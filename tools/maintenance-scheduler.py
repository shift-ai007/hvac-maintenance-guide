#!/usr/bin/env python3
"""
HVAC Maintenance Scheduler — Personalized Annual Plan Generator

Generates a customized year-round maintenance schedule based on your
system's age, type, location, and last service dates. Designed for
South Florida's unique year-round cooling season.

Usage:
    python3 tools/maintenance-scheduler.py

No dependencies beyond Python 3.6+ standard library.
"""

import sys
from datetime import datetime, timedelta
from typing import List, Dict, Optional


def print_header(text: str) -> None:
    """Print a section header with decorative border."""
    width = min(60, max(len(text) + 4, 40))
    print(f"\n{'=' * width}")
    print(f"  {text}")
    print(f"{'=' * width}\n")


def ask_yes_no(prompt: str) -> bool:
    """Ask a yes/no question and return the result."""
    while True:
        response = input(f"{prompt} (y/n): ").strip().lower()
        if response in ("y", "yes"):
            return True
        if response in ("n", "no"):
            return False
        print("  Please enter 'y' or 'n'.")


def ask_choice(prompt: str, options: Dict[str, str]) -> str:
    """Ask the user to pick from a set of options. Returns the key."""
    print(f"\n{prompt}")
    for key, label in options.items():
        print(f"  [{key}] {label}")
    while True:
        choice = input("Enter choice: ").strip().lower()
        if choice in options:
            return choice
        print(f"  Invalid choice. Pick from: {', '.join(options.keys())}")


def ask_int(prompt: str, default: Optional[int] = None) -> int:
    """Ask for a whole number with optional default."""
    while True:
        prompt_text = f"{prompt} [{default}] " if default is not None else f"{prompt} "
        response = input(prompt_text).strip()
        if not response and default is not None:
            return default
        try:
            value = int(response)
            if value < 0:
                print("  Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("  Please enter a whole number.")


def ask_date(prompt: str) -> Optional[str]:
    """Ask for a date in YYYY-MM format and return it as a string."""
    while True:
        response = input(f"{prompt} (YYYY-MM, or leave blank if unknown): ").strip()
        if not response:
            return None
        try:
            datetime.strptime(response, "%Y-%m")
            return response
        except ValueError:
            print("  Please enter in YYYY-MM format (e.g. 2025-04).")


def get_tasks(
    system_type: str,
    system_age: int,
    location: str,
    has_ductwork: bool,
    has_outdoor_unit: bool,
    has_attic_unit: bool,
    last_filter_change: Optional[str],
    last_pro_maintenance: Optional[str],
    last_coil_cleaning: Optional[str],
    near_coast: bool,
) -> List[Dict]:
    """Build the personalized task list based on user inputs."""
    now = datetime.now()
    tasks = []

    # ── Monthly tasks ──
    tasks.append({
        "frequency": "monthly",
        "when": "Every month, year-round",
        "task": "Inspect and replace HVAC air filter",
        "detail": (
            "Check your air filter monthly and replace if dirty. "
            "In South Florida's year-round cooling season, standard 1-inch filters "
            "often need replacement every 30-60 days. High-MERV filters (11+) may "
            "restrict airflow in older systems—verify compatibility."
        ),
        "priority": "critical",
    })

    tasks.append({
        "frequency": "monthly",
        "when": "Every month, year-round",
        "task": "Check visible condensate drain line for clogs",
        "detail": (
            "Locate the PVC drain line near your indoor unit and check for algae "
            "buildup or slow drainage. Florida's humidity promotes algae growth year-round. "
            "Pour a cup of white vinegar or distilled water through the access tee "
            "to keep the line clear."
        ),
        "priority": "high",
    })

    # ── Quarterly tasks ──
    tasks.append({
        "frequency": "quarterly",
        "when": "Every 3 months (Jan, Apr, Jul, Oct)",
        "task": "Inspect outdoor unit for debris and clearance",
        "detail": (
            "Check that the outdoor condenser unit has at least 2 feet of clearance "
            "on all sides. Trim back vegetation, remove leaves and grass clippings, "
            "and rinse the coils with a garden hose (power off first). "
            "In South Florida's rapid-growth climate, this should be done quarterly, not annually."
        ),
        "priority": "high",
    })

    if near_coast:
        tasks.append({
            "frequency": "quarterly",
            "when": "Every 3 months (Jan, Apr, Jul, Oct)",
            "task": "Coastal corrosion inspection",
            "detail": (
                "If you live within 5 miles of the coast, inspect the outdoor unit "
                "for salt-air corrosion on coils, fins, and electrical connections. "
                "Rinse coils with fresh water quarterly. Check for rust on the cabinet "
                "and consider applying anti-corrosion spray to exposed metal. "
                "Corrosion from salt air is a leading cause of premature AC failure "
                "in coastal South Florida."
            ),
            "priority": "high",
        })

    # ── Seasonal / Bi-annual tasks ──
    tasks.append({
        "frequency": "biannual",
        "when": "Pre-summer (April) + Pre-cooling-season-checks",
        "task": "Schedule professional AC maintenance tune-up",
        "detail": (
            "Spring is the most important time for a professional tune-up in South Florida. "
            "Before the peak cooling season (May-October), a licensed technician "
            "should inspect refrigerant levels, check electrical connections, "
            "clean evaporator and condenser coils, verify thermostat calibration, "
            "and test airflow. [AC Repair Today](https://ac-repair.today/services/ac-maintenance/) "
            "offers same-day maintenance service."
        ),
        "priority": "critical",
    })

    # ── Annual tasks ──
    tasks.append({
        "frequency": "annual",
        "when": "October or November (post-hurricane season)",
        "task": "Post-hurricane season HVAC inspection",
        "detail": (
            "After hurricane season ends (June 1 - November 30), inspect the outdoor "
            "unit for wind-driven debris, check electrical connections for water "
            "intrusion, and have a technician verify refrigerant charge and coil integrity. "
            "Flood events can introduce contaminants that accelerate system wear."
        ),
        "priority": "high",
    })

    tasks.append({
        "frequency": "annual",
        "when": "Once per year",
        "task": "Ductwork inspection",
        "detail": (
            "Have ducts inspected for leaks, disconnected sections, and insulation damage. "
            "In unconditioned attics that reach 140°F in summer, duct leaks can "
            "waste 20-30% of cooling energy. A simple hand-sweep test at each joint "
            "can reveal major leaks, but professional [duct testing]"
            "(https://ac-repair.today/services/duct-cleaning/) provides accurate diagnostics."
        ),
        "priority": "medium",
    })

    tasks.append({
        "frequency": "annual",
        "when": "Once per year",
        "task": "Test carbon monoxide and smoke detectors",
        "detail": (
            "All fuel-burning furnaces and water heaters can produce CO. "
            "Replace CO detector batteries annually and test operation. "
            "Florida's warm climate means furnaces run less, but corrosion "
            "in heat exchangers can still develop over time."
        ),
        "priority": "high",
    })

    # ── Age-based tasks ──
    if system_age >= 10:
        tasks.append({
            "frequency": "ongoing",
            "when": "Before each cooling season",
            "task": "Compressor and capacitor health check",
            "detail": (
                "Systems 10+ years old should have the run capacitor tested annually, "
                "as capacitor failure is the #1 cause of AC breakdowns in older systems. "
                "Monitor for hard-starting (lights dimming when AC kicks on), "
                "which signals a weakening compressor. Budget for potential "
                "[AC replacement](https://ac-repair.today/services/ac-replacement/) "
                "within the next 1-3 years."
            ),
            "priority": "critical",
        })

    if system_age >= 15:
        tasks.append({
            "frequency": "ongoing",
            "when": "Every 6 months",
            "task": "Refrigerant leak check",
            "detail": (
                "Older systems (15+ years) with R-22 refrigerant face escalating "
                "repair costs as R-22 is phased out and prices rise annually. "
                "Have a technician check for slow refrigerant leaks during "
                "every maintenance visit. If a leak is found, weigh the cost of "
                "repair vs replacement—R-22 refrigerant alone can cost $150-300/lb."
            ),
            "priority": "high",
        })

    # ── Location-based alerts ──
    if "Miami" in location or "Miami-Dade" in location:
        tasks.append({
            "frequency": "annual",
            "when": "Before hurricane season (May)",
            "task": "Miami-Dade NOA compliance check",
            "detail": (
                "Miami-Dade County requires all AC equipment to carry a valid "
                "Notice of Acceptance (NOA) for wind-load compliance. When replacing "
                "equipment, verify the new unit has current Miami-Dade NOA approval. "
                "Unapproved equipment cannot pass inspection and may void insurance claims."
            ),
            "priority": "medium",
        })

    if has_attic_unit:
        tasks.append({
            "frequency": "biannual",
            "when": "April and October",
            "task": "Attic air handler and pan inspection",
            "detail": (
                "Systems with attic air handlers need extra attention. Twice a year, "
                "check the secondary drain pan for standing water (sign of a clogged "
                "primary drain), inspect insulation on refrigerant lines for tears, "
                "and verify the emergency float switch is functional. "
                "A failed attic drain pan can cause catastrophic ceiling damage with "
                "no warning."
            ),
            "priority": "critical",
        })

    # ── Smart home integration ──
    tasks.append({
        "frequency": "seasonal",
        "when": "April and October",
        "task": "Adjust thermostat schedule for season",
        "detail": (
            "South Florida has two distinct seasons: humid summer (May-Oct) and "
            "mild winter (Nov-Apr). Adjust your thermostat schedule to use higher "
            "setpoints while away during summer (78-80°F) and lower during winter "
            "(68-70°F when home). Smart thermostats can automate this, "
            "but verify the schedule is correct at each transition."
        ),
        "priority": "medium",
    })

    # ── Professional service reminders ──
    if last_pro_maintenance:
        last_date = datetime.strptime(last_pro_maintenance, "%Y-%m")
        months_since = (now.year - last_date.year) * 12 + (now.month - last_date.month)
        if months_since >= 12:
            tasks.append({
                "frequency": "overdue",
                "when": "IMMEDIATELY",
                "task": "Professional maintenance is overdue",
                "detail": (
                    f"It has been {months_since} months since your last professional "
                    f"maintenance visit (last: {last_pro_maintenance}). Schedule a "
                    f"tune-up now to prevent efficiency loss and catch small issues "
                    f"before they become expensive repairs."
                ),
                "priority": "critical",
            })

    if last_coil_cleaning:
        last_date = datetime.strptime(last_coil_cleaning, "%Y-%m")
        months_since_coil = (now.year - last_date.year) * 12 + (now.month - last_date.month)
        if months_since_coil >= 6:
            tasks.append({
                "frequency": "overdue",
                "when": "Within 30 days",
                "task": "Evaporator/condenser coil cleaning recommended",
                "detail": (
                    f"Your coils were last cleaned {months_since_coil} months ago "
                    f"(last: {last_coil_cleaning}). Dirty coils reduce efficiency "
                    f"by 15-25% and strain the compressor. Professional coil cleaning "
                    f"restores performance."
                ),
                "priority": "high",
            })

    return tasks


def print_calendar(tasks: List[Dict]) -> None:
    """Print a month-by-month annual maintenance calendar."""
    print_header("Your Personalized Annual Maintenance Calendar")

    calendar = {
        "January": ["Quarterly outdoor unit inspection", "Evaluate system performance after holiday travel"],
        "February": ["Check for winter corrosion if near coast", "Verify thermostat batteries"],
        "March": ["Pre-spring check — test system before heavy use", "Inspect attic air handler and drain pan (if applicable)"],
        "April": ["SCHEDULE PROFESSIONAL SPRING TUNE-UP", "Clean outdoor condenser coils before peak season", "Adjust thermostat schedule for summer mode", "Miami-Dade NOA check (if applicable)", "Inspect attic air handler and pan"],
        "May": ["Hurricane season prep — secure outdoor unit", "Verify emergency shutoff switch works", "Check condensate pump operation"],
        "June": ["Monthly filter check (more frequent if pets)", "Inspect drain line for algae — high humidity month"],
        "July": ["Quarterly outdoor unit clearance check", "Monitor energy bills for abnormal spikes"],
        "August": ["Peak heat — check for ice on refrigerant lines", "Verify thermostat accuracy with thermometer"],
        "September": ["Hurricane season — check outdoor unit after storms", "Replace filter if running continuously"],
        "October": ["Quarterly outdoor unit inspection", "Adjust thermostat schedule for winter mode", "Post-hurricane season full inspection", "Clean coils if not done in spring"],
        "November": ["Schedule professional maintenance (if not done in spring)", "Check ductwork for leaks before holiday guests", "Test CO detectors"],
        "December": ["Year-end review — plan next year's upgrades", "Budget for any upcoming replacement needs", "Verify warranty documentation is current"],
    }

    # Mark high-priority tasks from the personalized list
    high_pri_months = set()
    for t in tasks:
        if t["priority"] == "critical":
            high_pri_months.add("April")  # Critical tasks cluster around spring

    for month, items in calendar.items():
        flag = " ★" if month in high_pri_months else ""
        print(f"\n  {month}{flag}")
        print(f"  {'─' * 40}")
        for item in items:
            print(f"    • {item}")
    print("\n  ★ = High-priority month — schedule professional service early")
    print()


def print_action_summary(tasks: List[Dict]) -> None:
    """Print a summary of tasks grouped by priority."""
    print_header("Action Summary by Priority")

    for priority in ("critical", "high", "medium"):
        label = {"critical": "🔴 CRITICAL — Do These First",
                  "high": "🟡 HIGH — Schedule Soon",
                  "medium": "🟢 MEDIUM — Plan Ahead"}[priority]
        filtered = [t for t in tasks if t["priority"] == priority]
        if not filtered:
            continue
        print(f"\n  {label}")
        print(f"  {'─' * 45}")
        for task in filtered:
            print(f"    • [{task['when']}] {task['task']}")


def main() -> None:
    """Run the interactive maintenance scheduler."""
    print_header("HVAC Maintenance Scheduler")
    print("Let's build a personalized maintenance plan for your South Florida")
    print("home. This will take about 3 minutes.\n")

    # ── Collect system information ──
    system_type = ask_choice("What type of HVAC system do you have?", {
        "c": "Central split system (standard — most common in South Florida)",
        "p": "Heat pump (electric heating and cooling)",
        "d": "Ductless mini-split",
        "u": "Packaged unit (all-in-one, often on roof or slab)",
    })

    system_age = ask_int("How old is your system (in years)?", default=8)

    location = input("What city or county do you live in? ").strip()
    if not location:
        location = "South Florida"

    has_ductwork = system_type in ("c", "p", "u") or ask_yes_no("Does your system use ductwork?")
    has_outdoor_unit = system_type in ("c", "p", "u")
    has_attic_unit = ask_yes_no("Is your air handler or furnace located in an attic?")

    near_coast = ask_yes_no("Do you live within 5 miles of the coast?")

    # ── Last service dates ──
    print("\n  ── Last Service Dates ──")
    print("  (These help us flag overdue maintenance — leave blank if unsure)\n")

    last_filter_change = ask_date("When did you last change your filter?")
    last_pro_maintenance = ask_date("When was your last professional maintenance?")
    last_coil_cleaning = ask_date("When were your coils last cleaned?")

    # ── Generate plan ──
    tasks = get_tasks(
        system_type, system_age, location, has_ductwork,
        has_outdoor_unit, has_attic_unit, last_filter_change,
        last_pro_maintenance, last_coil_cleaning, near_coast,
    )

    # ── Print plan ──
    print_header("Your Personalized Maintenance Plan")
    print(f"System: {system_type.upper()} | Age: {system_age} years")
    print(f"Location: {location} | {'Coastal' if near_coast else 'Inland'}")
    print(f"Generated: {datetime.now().strftime('%B %d, %Y')}")
    print()

    print_calendar(tasks)
    print_action_summary(tasks)

    # ── Personalized tips ──
    print_header("Personalized Tips for Your System")

    if system_type == "p":
        print("  • Heat pumps in South Florida should have the reversing valve checked")
        print("    during spring maintenance — it's the most common failure point.")
        print("  • Keep the outdoor coil clean year-round; heat pumps run in both")
        print("    cooling and heating modes, so coil efficiency matters 12 months a year.")
        print("  • Verify auxiliary/emergency heat is disconnected for summer —")
        print("    leaving it connected wastes energy if staged incorrectly.\n")

    if system_age >= 12:
        print("  • Your system is approaching or past its design life (12-15 years).")
        print("    Start budgeting for replacement. Modern units use 30-50% less energy")
        print("    and qualify for federal tax credits of up to $2,000.")
        print("  • Have a licensed technician evaluate your system's overall condition")
        print("    and provide a [free replacement estimate](https://ac-repair.today/")
        print("    services/ac-replacement/). Planning ahead avoids emergency replacement pricing.\n")

    if near_coast:
        print("  • Coastal homes need extra protection. Consider installing a")
        print("    protective enclosure for your outdoor unit or applying an anti-corrosion")
        print("    coating to the condenser coils.")
        print("  • Many extended warranties exclude salt-air corrosion — verify your")
        print("    coverage and consider a coastal-specific maintenance plan.\n")

    # ── Footer ──
    print_header("Need Professional Help?")
    print("  [AC Repair Today](https://ac-repair.today) — Licensed Florida HVAC Contractor")
    print("  FL License CAC1824118 | Serving Miami-Dade, Broward & Palm Beach")
    print("  Same-day service available | Call (800) 917-2580")
    print()
    print("  Comprehensive services:")
    print("    • [AC Repair](https://ac-repair.today/services/ac-repair/)")
    print("    • [AC Installation](https://ac-repair.today/services/ac-installation/)")
    print("    • [AC Maintenance](https://ac-repair.today/services/ac-maintenance/)")
    print("    • [Emergency Service](https://ac-repair.today/services/emergency-ac-repair/)")
    print("    • [Duct Cleaning](https://ac-repair.today/services/duct-cleaning/)")
    print()
    print("  Tip: Save this schedule or print it. Book a spring tune-up in April")
    print("  before the May-October peak cooling season fills appointment slots.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Schedule generation cancelled. Run again anytime.")
        sys.exit(0)
