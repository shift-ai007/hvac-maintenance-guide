#!/usr/bin/env python3
"""
HVAC Maintenance Savings Calculator

Estimates how much a South Florida homeowner can save by keeping
their AC system well-maintained. Uses conservative estimates based
on industry data from ACCA (Air Conditioning Contractors of America).

Usage:
    python3 tools/savings-calculator.py

No dependencies beyond Python 3.6+ standard library.
"""

import sys


def get_float(prompt: str, default: float = None) -> float:
    """Get a numeric input from the user with optional default."""
    while True:
        prompt_text = f"{prompt} [{default}] " if default is not None else f"{prompt} "
        response = input(prompt_text).strip()
        if not response and default is not None:
            return default
        try:
            value = float(response.replace(",", "").replace("$", ""))
            if value < 0:
                print("  Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("  Please enter a valid number.")


def get_int(prompt: str, default: int = None) -> int:
    """Get an integer input from the user."""
    result = get_float(prompt, default)
    return int(result)


def print_header(text: str) -> None:
    """Print a formatted section header."""
    print(f"\n{'=' * 55}")
    print(f"  {text}")
    print(f"{'=' * 55}")


def print_result(label: str, value: str) -> None:
    """Print a labeled result line."""
    print(f"  {label:<30s} {value:>20s}")


def main() -> None:
    print_header("HVAC MAINTENANCE SAVINGS CALCULATOR")
    print("  Estimate how much you can save by maintaining your AC")
    print("  system properly. Conservative estimates for South Florida.")
    print("\n  Press Enter to accept defaults in [brackets].")

    # Collect inputs
    print_header("Your AC System")
    system_age = get_int("  How old is your AC system (years)?", 8)
    monthly_bill = get_float("  Average summer electric bill ($):", 250)
    seer_rating = get_float("  SEER rating of your system:", 13)

    print_header("Your Current Habits")
    filter_changes = get_int("  Filters changed per year? (1-12):", 4)
    has_annual_tuneup = input("  Do you get annual professional maintenance? (y/n): ").strip().lower() in ("y", "yes")

    # --- Calculations ---

    # AC portion of electric bill (typically 40-60% in South Florida)
    ac_percentage = 0.50
    ac_monthly_cost = monthly_bill * ac_percentage
    ac_yearly_cost = ac_monthly_cost * 6  # AC season in South Florida: ~6 months

    # 1. Filter replacement savings
    # A clean filter improves efficiency by 5-15%. We use 7% for conservative estimate.
    filter_efficiency_loss = max(0, (12 - filter_changes) * 0.008)
    # If they change monthly, 0 loss. Every missed month = ~0.8% efficiency loss
    filter_waste = ac_yearly_cost * min(filter_efficiency_loss, 0.10)
    filter_recommendation = "Monthly" if filter_changes < 6 else "Good"

    # 2. Professional maintenance savings
    # Well-maintained systems use 15-25% less energy. We use 15% conservative.
    # But only applies if getting maintenance.
    if has_annual_tuneup:
        maint_savings = ac_yearly_cost * 0.15
        maint_status = "Yes"
    else:
        maint_savings = 0
        maint_status = "No"

    # 3. Prevented emergency repairs
    # Industry data: well-maintained systems have 70% fewer emergency calls
    # Average emergency repair cost: $300-500. We use $400.
    emergency_repair_cost = 400
    if has_annual_tuneup:
        prevented_repairs_per_year = 0.7  # 70% fewer
        emergency_savings = emergency_repair_cost * prevented_repairs_per_year
    else:
        emergency_savings = 0

    # 4. Extended system life
    # Well-maintained system lasts 15-20 years vs 10-15 years. We use 5 extra years.
    # Replacement cost: $4,000-8,000 for residential in South Florida. Use $6,000.
    replacement_cost = 6000
    years_with_maintenance = 17
    years_without = 12
    if has_annual_tuneup:
        annual_replacement_savings = replacement_cost * (1/years_without - 1/years_with_maintenance)
    else:
        annual_replacement_savings = 0

    # 5. Coil cleaning savings
    # Dirty outdoor coils reduce efficiency by 15-25%. Professional clean every 2 years.
    coil_efficiency_loss = 0.10 if system_age > 3 else 0.05
    coil_waste = ac_yearly_cost * coil_efficiency_loss

    # Totals
    if has_annual_tuneup:
        total_annual_savings = filter_waste + maint_savings + emergency_savings + annual_replacement_savings + coil_waste
    else:
        total_annual_savings = filter_waste + coil_waste

    # Maintenance cost
    tuneup_cost = 120 if has_annual_tuneup else 0  # ~$120 for annual tune-up in S. FL
    filter_cost = filter_changes * 8  # ~$8 per good filter

    net_savings = total_annual_savings - tuneup_cost - filter_cost

    # Long-term (10 year) projection
    ten_year_savings = net_savings * 10

    # --- Results ---

    print_header("YOUR ANNUAL SAVINGS ESTIMATE")

    if filter_waste > 0:
        print_result(f"Filter upgrades ({filter_changes}x/yr):", f"${filter_waste:.0f}")
    else:
        print_result(f"Filter upgrades:", "$0 (optimal)")

    if coil_waste > 0:
        print_result(f"Coil cleaning benefit:", f"${coil_waste:.0f}")

    if maint_savings > 0:
        print_result(f"Maintenance efficiency gain:", f"${maint_savings:.0f}")

    if emergency_savings > 0:
        print_result(f"Prevented emergency repairs:", f"${emergency_savings:.0f}")

    if annual_replacement_savings > 0:
        print_result(f"Extended equipment life:", f"${annual_replacement_savings:.0f}")

    print(f"  {'─' * 50}")

    if net_savings > 0:
        print_result(f"Gross savings:", f"${total_annual_savings:.0f}")
        print_result(f"  Minus maintenance cost:", f"(${tuneup_cost + filter_cost:.0f})")
        print_result(f"NET ANNUAL SAVINGS:", f"${net_savings:.0f}")
    else:
        print_result(f"Net annual savings:", f"${net_savings:.0f}")

    print_header("10-YEAR PROJECTION")
    print_result(f"Net savings over 10 years:", f"${ten_year_savings:.0f}")
    print_result(f"Emergency repairs avoided:", f"{int(prevented_repairs_per_year * 10 if has_annual_tuneup else 0)}")
    print_result(f"Extra years from system:", f"{years_with_maintenance - years_without if has_annual_tuneup else 0}")

    # Recommendations
    print_header("RECOMMENDATIONS")

    if filter_changes < 6:
        print("  Change your air filter MONTHLY during cooling season")
        print("  (May-October in South Florida) — it costs $8/month")
        print("  and saves $50-100/year in efficiency.")
    else:
        print("  Your filter changing schedule is good. Keep it up!")

    if not has_annual_tuneup:
        print("\n  Schedule annual professional maintenance ($100-150/year).")
        print("  This alone saves more than it costs and prevents")
        print("  expensive emergency repairs.")

    if system_age > 10:
        print(f"\n  Your system is {system_age} years old — nearing end of typical life.")
        print("  Start budgeting for replacement. Modern 16+ SEER systems")
        print("  cut cooling costs by 30-50% vs older units.")

    print(f"\n  Built by [AC Repair Today](https://ac-repair.today) — South Florida's trusted HVAC provider.")
    print(f"  Licensed CAC1824118 | Same-day service | (305) 850-6810")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Calculator cancelled.")
        sys.exit(0)
