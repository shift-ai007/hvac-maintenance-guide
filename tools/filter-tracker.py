#!/usr/bin/env python3
"""
AC Filter Replacement Tracker — Keep Track of Filter Changes Across Your Home

Most HVAC problems start with a dirty filter. This tool helps homeowners
track filter changes across multiple AC units, know what filter size and
type each unit needs, and maintain a service history.

Usage:
    python3 tools/filter-tracker.py           # Interactive mode
    python3 tools/filter-tracker.py --status   # Show current status quickly

No dependencies beyond Python 3.6+ standard library.
"""

import json
import os
import sys
import time
from datetime import datetime, date, timedelta
from typing import Optional, List


DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "filter-data.json")


def print_header(text: str) -> None:
    """Print a section header."""
    width = min(60, max(len(text) + 4, 40))
    print(f"\n{'=' * width}")
    print(f"  {text}")
    print(f"{'=' * width}\n")


def get_default_units() -> list:
    """Return default filter units for a typical South Florida home."""
    return [
        {
            "name": "Main System",
            "filter_size": "20x20x1",
            "merv_rating": 8,
            "type": "Disposable pleated",
            "location": "Return grille, living room hallway",
            "replacement_interval_months": 1,
            "notes": "Change monthly June–September",
        },
        {
            "name": "Upper Floor System",
            "filter_size": "16x25x1",
            "merv_rating": 8,
            "type": "Disposable pleated",
            "location": "Return grille, upstairs landing",
            "replacement_interval_months": 1,
            "notes": "",
        },
    ]


def load_data() -> dict:
    """Load filter tracking data from JSON file."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE) as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass

    return {
        "units": get_default_units(),
        "history": [],
        "created_at": date.today().isoformat(),
        "updated_at": date.today().isoformat(),
    }


def save_data(data: dict) -> None:
    """Save filter tracking data to JSON file."""
    data["updated_at"] = date.today().isoformat()
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
    print(f"\n  ✓ Data saved to {DATA_FILE}")


def print_merv_guide() -> None:
    """Print a guide to MERV ratings."""
    print_header("MERV Rating Guide")
    print("  The Minimum Efficiency Reporting Value (MERV) measures a filter's")
    print("  ability to capture particles of different sizes.")
    print()
    print("  MERV 1-4:   Window AC / basic — stops lint, dust mites")
    print("              ❌ TOO LOW for central AC — lets fine dust through")
    print("  MERV 5-6:   Standard fiberglass — stops mold spores, dust")
    print("              ✓ Minimum for central AC systems")
    print("  MERV 7-8:   Better pleated — stops pollen, dust mite debris")
    print("              ✓ RECOMMENDED for most South Florida homes")
    print("              ✓ Good balance of protection + airflow")
    print("  MERV 9-12:  Premium — stops fine dust, lead dust, auto emissions")
    print("              ⚠ May restrict airflow on older systems")
    print("  MERV 13-16: Hospital-grade — stops bacteria, smoke, virus carriers")
    print("              ⚠ ONLY if HVAC system was designed for it")
    print("              ❌ Can damage older equipment (reduced airflow)")
    print()
    print("  Rule of thumb for South Florida homes:")
    print("  - System installed before 2010: MERV 8 (or MERV 6 if airflow is weak)")
    print("  - System installed 2010–2020: MERV 8")
    print("  - System installed 2020+: MERV 8–11 (check manual)")
    print("  - Allergy concerns + newer system: MERV 11")
    print("  - NEVER go above MERV 13 unless manual specifically allows it")
    print()
    print("  High MERV + dirty filter = frozen coil + expensive repair.")
    print("  Better to change a MERV 8 monthly than run a MERV 13 for 3 months.")


def ask_yes_no(prompt: str) -> bool:
    """Ask a yes/no question."""
    while True:
        response = input(f"{prompt} (y/n): ").strip().lower()
        if response in ("y", "yes"):
            return True
        if response in ("n", "no"):
            return False
        print("  Please answer 'y' or 'n'.")


def ask_int(prompt: str, default: Optional[int] = None, min_val: int = 1, max_val: int = 999) -> int:
    """Ask for an integer input."""
    while True:
        d = f" [{default}]" if default else ""
        response = input(f"{prompt}{d}: ").strip()
        if not response and default is not None:
            return default
        try:
            val = int(response)
            if min_val <= val <= max_val:
                return val
            print(f"  Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("  Please enter a valid number.")


def print_status(data: dict) -> None:
    """Print the current filter status for all units."""
    print_header("Filter Status Overview")

    if not data["units"]:
        print("  No units configured. Run the interactive setup first.")
        return

    today = date.today()

    for unit in data["units"]:
        name = unit["name"]
        size = unit["filter_size"]
        merv = unit["merv_rating"]
        interval = unit["replacement_interval_months"]

        # Find last replacement for this unit
        last_change = None
        for entry in reversed(data.get("history", [])):
            if entry.get("unit") == name and entry.get("event") == "replace":
                last_change = date.fromisoformat(entry["date"])
                break

        print(f"  ┌─ {name}")
        print(f"  │ Filter: {size}, MERV {merv} — {unit.get('type', 'pleated')}")
        print(f"  │ Location: {unit.get('location', 'N/A')}")
        print(f"  │ Change interval: every {interval} month{'s' if interval > 1 else ''}")

        if last_change:
            days_since = (today - last_change).days
            days_target = interval * 30
            pct = (days_since / days_target) * 100
            due_date = last_change + timedelta(days=days_target)

            if days_since >= days_target:
                overdue = days_since - days_target
                print(f"  │ ⚠ OVERDUE — Last changed: {last_change.isoformat()} ({days_since} days ago)")
                print(f"  │   Was due: {due_date.isoformat()} ({overdue} days overdue)")
            elif pct >= 80:
                print(f"  │ ⚡ Due soon — Last changed: {last_change.isoformat()} ({days_since} days ago)")
                print(f"  │   Due by: {due_date.isoformat()} ({days_target - days_since} days remaining)")
            else:
                print(f"  │ ✓ OK — Last changed: {last_change.isoformat()} ({days_since} days ago)")
                print(f"  │   Due by: {due_date.isoformat()} ({days_target - days_since} days remaining)")
        else:
            print(f"  │ ⚠ No replacement recorded yet")
            print(f"  │   Change it now if it's been more than {interval} month(s)!")

        if unit.get("notes"):
            print(f"  │ Notes: {unit['notes']}")
        print(f"  └─")

    print()
    print("  Pro tip: Write the date on your new filter with a marker so")
    print("  you can see at a glance whether it needs changing.")
    print()
    print(f"  For professional AC maintenance: https://ac-repair.today/services/ac-maintenance/")


def record_change(data: dict) -> None:
    """Record a filter replacement."""
    print_header("Record Filter Change")

    if not data["units"]:
        print("  No units configured yet. Set them up first.")
        return

    print("  Which unit did you change?")
    for i, unit in enumerate(data["units"], 1):
        print(f"  {i}. {unit['name']} — {unit['filter_size']} MERV {unit['merv_rating']}")

    choice = ask_int("Select unit", min_val=1, max_val=len(data["units"]))
    unit = data["units"][choice - 1]

    print()
    print(f"  Recorded change for: {unit['name']} ({unit['filter_size']})")

    # Auto-detect filter size from what was previously set
    if ask_yes_no(f"  Did you use a {unit['filter_size']} MERV {unit['merv_rating']} filter?"):
        size = unit["filter_size"]
        merv = unit["merv_rating"]
    else:
        size = input("  What size filter? (e.g. 20x20x1): ").strip()
        merv = ask_int("  What MERV rating", default=unit["merv_rating"], min_val=1, max_val=16)

    notes = input("  Any notes? (brand, price, issues — or press Enter): ").strip()

    entry = {
        "event": "replace",
        "unit": unit["name"],
        "date": date.today().isoformat(),
        "filter_size": size,
        "merv_rating": merv,
        "notes": notes if notes else "",
    }

    data.setdefault("history", []).append(entry)

    if ask_yes_no("  Also set this filter as the default for this unit?"):
        unit["filter_size"] = size
        unit["merv_rating"] = merv

    save_data(data)
    print(f"  ✓ Recorded: {unit['name']} filter changed {date.today().isoformat()}")
    print()
    print(f"  Next change due approximately: {(date.today() + timedelta(days=unit['replacement_interval_months'] * 30)).isoformat()}")


def configure_units(data: dict) -> None:
    """Add, edit, or remove filter units."""
    print_header("Configure Your Systems")

    while True:
        print(f"  Current units ({len(data['units'])}):")
        for i, unit in enumerate(data["units"], 1):
            print(f"  {i}. {unit['name']} — {unit['filter_size']} MERV {unit['merv_rating']}")
            print(f"     Change every {unit['replacement_interval_months']} month(s)")
        print()
        print("  Options:")
        print("  1. Add a new unit")
        print("  2. Edit an existing unit")
        print("  3. Remove a unit")
        print("  4. View MERV rating guide")
        print("  5. Done — return to main menu")

        choice = ask_int("Select", default=5, min_val=1, max_val=5)

        if choice == 1:
            name = input("  System name (e.g. 'Main Floor', 'Downstairs'): ").strip()
            size = input("  Filter size (e.g. 20x20x1): ").strip()
            merv = ask_int("  MERV rating", default=8, min_val=1, max_val=16)
            interval = ask_int("  Change interval (months)", default=1, min_val=1, max_val=12)
            data["units"].append({
                "name": name,
                "filter_size": size,
                "merv_rating": merv,
                "type": "Disposable pleated",
                "location": input("  Location of return grille: ").strip(),
                "replacement_interval_months": interval,
                "notes": "",
            })
            save_data(data)
            print(f"  ✓ Added {name}")

        elif choice == 2:
            if not data["units"]:
                print("  No units to edit.")
                continue
            idx = ask_int("  Which unit to edit?", min_val=1, max_val=len(data["units"])) - 1
            unit = data["units"][idx]
            print(f"  Editing: {unit['name']}")
            unit["name"] = input(f"  Name [{unit['name']}]: ").strip() or unit["name"]
            unit["filter_size"] = input(f"  Filter size [{unit['filter_size']}]: ").strip() or unit["filter_size"]
            unit["merv_rating"] = ask_int("  MERV rating", default=unit["merv_rating"], min_val=1, max_val=16)
            unit["replacement_interval_months"] = ask_int("  Change interval (months)", default=unit["replacement_interval_months"], min_val=1, max_val=12)
            save_data(data)
            print(f"  ✓ Updated {unit['name']}")

        elif choice == 3:
            if not data["units"]:
                print("  No units to remove.")
                continue
            idx = ask_int("  Which unit to remove?", min_val=1, max_val=len(data["units"])) - 1
            name = data["units"][idx]["name"]
            if ask_yes_no(f"  Remove '{name}'?"):
                data["units"].pop(idx)
                save_data(data)
                print(f"  ✓ Removed {name}")

        elif choice == 4:
            print_merv_guide()

        elif choice == 5:
            break


def show_history(data: dict) -> None:
    """Show filter change history."""
    print_header("Filter Change History")

    if not data.get("history"):
        print("  No changes recorded yet.")
        return

    for entry in data["history"]:
        print(f"  {entry['date']} — {entry['unit']}: {entry['filter_size']} MERV {entry['merv_rating']}")
        if entry.get("notes"):
            print(f"    Notes: {entry['notes']}")

    print(f"\n  Total changes recorded: {len(data['history'])}")


def interactive_mode() -> None:
    """Run the filter tracker in interactive mode."""
    data = load_data()

    print_header("AC Filter Replacement Tracker")
    print("  Track filter changes across all your AC units.")
    print("  Get alerts when it's time for a replacement.")
    print()

    while True:
        print()
        print("  ┌─ Main Menu ─────────────────────────────┐")
        print("  │ 1. View filter status (all units)       │")
        print("  │ 2. Record a filter change               │")
        print("  │ 3. Configure your systems/units         │")
        print("  │ 4. View replacement history             │")
        print("  │ 5. MERV rating guide                    │")
        print("  │ 6. Exit                                 │")
        print("  └─────────────────────────────────────────┘")

        choice = ask_int("Select", default=1, min_val=1, max_val=6)

        if choice == 1:
            print_status(data)
        elif choice == 2:
            record_change(data)
        elif choice == 3:
            configure_units(data)
        elif choice == 4:
            show_history(data)
        elif choice == 5:
            print_merv_guide()
        elif choice == 6:
            print("\n  Don't forget to check your filters!")
            print(f"  For professional AC maintenance: https://ac-repair.today/services/ac-maintenance/")
            break


def quick_status() -> None:
    """Show quick filter status without interactive mode."""
    data = load_data()
    print_status(data)


def main():
    if len(sys.argv) > 1 and sys.argv[1] in ("--status", "-s"):
        quick_status()
    elif not sys.stdin.isatty():
        print("Run without arguments for interactive mode, or use --status for quick status.")
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
