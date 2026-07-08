# Home Buyer's AC Inspection Checklist for South Florida

Buying a home in South Florida means inheriting its AC system — and in our climate, that system runs 8-10 months a year. A failing AC that looks fine during a showing can cost $5,000-12,000 to replace within your first year of ownership. This guide covers what every home buyer should check before closing, what a standard home inspection often misses, and how to evaluate whether a system has years of life left or is running on borrowed time.

## Why Standard Home Inspections Miss AC Problems

Most general home inspectors perform a limited HVAC check: they verify the system turns on, measure supply vent temperature, and note the unit's age. This surface-level inspection catches obvious failures but misses the slow-moving problems that kill systems within 12-24 months.

In South Florida specifically:
- **Condenser coil condition is rarely inspected** — inspectors look through the grille and call it "visibly acceptable" without removing the fan grille to check for hidden corrosion
- **Refrigerant charge is not measured** — an AC can cool adequately at 80% charge while the compressor runs hotter and shortens its life by years
- **Duct leakage in the attic goes undetected** — Florida's 140°F attics hide duct leaks that cost $50-100/month in wasted energy
- **Permit history is almost never checked** — an unpermitted compressor replacement means the system may not meet current code

## Pre-Offer Research (Before You Tour)

### Check the AC Permit History

Every AC replacement, new installation, and major component replacement in Florida requires a permit from the local building department. You can check permit history online through most municipal portals:

- **Miami-Dade**: eMiamiDade building permit search
- **Broward**: Each city has its own system (Fort Lauderdale, Pembroke Pines, Hollywood portals)
- **Palm Beach**: Countywide ePermit portal

What to look for:
- A permit for the condenser unit (outdoor) matching the model/serial
- A permit for the air handler (indoor) matching the model/serial
- A finaled inspection (passed) — not just an issued permit
- If no permit exists: the work was done unlicensed, may not meet code, and you may be liable for bringing it up to code later

### Check the Manufacturer Date

The first 4-5 digits of the condenser's serial number encode the manufacture date. Most brands use YYWW format (year + week). A unit older than 10 years in South Florida is living on borrowed time — coastal corrosion accelerates every failure mode.

### Check the Contractor License

If a permit was pulled, note the contractor name and verify their Florida license at [myfloridalicense.com](https://www.myfloridalicense.com/wl11.asp). A lapsed or expired license on the install means no recourse if the work was defective.

## At the Showing — Exterior Inspection

### Condenser Unit (Outdoor)

| What to Check | Red Flags | What It Means |
|---------------|-----------|---------------|
| **Age** | Serial number decodes to >10 years old | Near or past expected lifespan in coastal climate |
| **Coil condition** | Fin corrosion covering >30% of coil area | Reduced efficiency, imminent refrigerant leaks |
| **Coil cleanliness** | Debris mat between fins, no light passes through | 15-25% efficiency loss, compressor working harder |
| **Cabinet rust** | Rust perforating the cabinet panels | Unit is nearing structural failure, replace soon |
| **Sound** | Loud buzzing, rattling, or screeching on startup | Failing contactor, fan motor bearings, or compressor |
| **Vibration** | Unit shakes visibly during operation | Compressor mount failure or internal damage |
| **Clearance** | Less than 24 inches on any side | Restricted airflow, premature failure |
| **Electrical disconnect** | Missing, rusted, or pull-out is stuck | Safety hazard, code violation |
| **Refrigerant lines** | Foam insulation is UV-cracked, bare copper showing | Efficiency loss, imminent line corrosion |

### How to Properly Check the Coils

Don't just glance through the grille. Ask the seller's agent for permission to remove the fan grille (4-6 screws, no tools needed beyond a screwdriver). This reveals:
- The true condition of the top 6-8 inches of coil
- Whether the fan blade is balanced and clean
- Whether the inside of the cabinet has standing water or debris
- Whether the coil fins are straight or crushed

If the seller refuses, consider it a yellow flag — what are they hiding?

## At the Showing — Interior Inspection

### Air Handler (Indoor Unit)

| What to Check | Red Flags | What It Means |
|---------------|-----------|---------------|
| **Location** | In attic, garage, or closet without a drain pan safety switch | Flood risk if drain clogs |
| **Pan condition** | Rusted, cracked, or standing water in the drain pan | Pan needs replacement, likely has leaked before |
| **Filter** | Dirty, wrong size, or missing | Poor maintenance history — expect other neglect |
| **Filter slot** | Gaps around filter (air bypassing) | Coil will be dirty, efficiency reduced |
| **Blower wheel** | Visible through slot, dirty/fur-wrapped | Airflow reduced 10-30%, motor working harder |
| **Drain line** | No visible trap, no safety switch | Code violation in most Florida jurisdictions |
| **Drain line material** | Metal pipe (galvanized steel) | Will rust internally within 5-7 years in Florida |
| **Insulation** | Duct insulation is sagging, torn, or missing | Massive energy loss, condensate dripping in attic |
| **Electrical** | Wiring is frayed, exposed, or uses wire nuts in wet location | Safety hazard, fire risk |

### Ductwork (Visible Sections)

Inspect any accessible ductwork in the attic, garage, or crawlspace:
- **Disconnected sections**: Common in Florida attics — animals or installers knock ducts off registers
- **Kinked flex duct**: Reduces airflow to that room by 30-70%
- **Sagging duct supports**: Flex duct should be supported every 4-5 feet; sagging creates low spots where condensate collects
- **Pest damage**: Rodent chew marks, wasp nests in duct openings
- **Insulation R-value**: Minimum R-8 in Florida attics (R-6 older construction). Less means $300-800/year extra cooling cost

### Thermostat

- **Location**: On an interior wall away from windows, kitchens, and supply vents
- **Type**: Programmable or smart (non-programmable on a newer system suggests cost-cutting)
- **Function**: Set to Cool, 78°F. Does the system respond within 5 minutes?
- **Consistency**: Temperature reading should match a standalone thermometer placed nearby

## The Runtime Test (Ask Permission)

If the seller allows, perform this 20-minute test:

1. Set thermostat to 78°F Cool, Fan AUTO
2. Note the time the compressor starts
3. After 15 minutes of operation:
   - Measure supply vent temperature (nearest vent to air handler)
   - Measure return temperature (at the filter grille)
   - **Delta T (temperature drop) should be 16-22°F** in South Florida
   - Below 14°F: low refrigerant, dirty coil, or airflow restriction
   - Above 24°F: very low airflow (dirty filter, undersized ducts, blower issue)
4. Let the system run until it satisfies the thermostat
   - A properly sized system in July should run 45-90 minutes to drop 4-5°F
   - Short cycles (<15 min) suggest oversized equipment or a problem
   - Runs >3 hours without satisfying: undersized or underperforming

### Measure the Temperature Drop

```python
# Quick delta-T calculator — runs in any Python 3 environment
supply = float(input("Supply vent temperature (°F): "))
return_air = float(input("Return grille temperature (°F): "))
delta = return_air - supply
if 16 <= delta <= 22:
    print(f"✓ Delta T = {delta:.1f}°F — Normal range for South Florida")
elif 14 <= delta < 16:
    print(f"⚠ Delta T = {delta:.1f}°F — Borderline low, may need service")
elif delta < 14:
    print(f"✗ Delta T = {delta:.1f}°F — Low — possible refrigerant leak, dirty coil, or airflow issue")
else:
    print(f"⚠ Delta T = {delta:.1f}°F — High — airflow restriction or metering device issue")
```

## Questions to Ask the Seller

1. **"How old is the AC system?"** — Cross-reference with serial number; don't trust verbal answers
2. **"When was the last service?"** — Look for a dated sticker on the condenser or air handler
3. **"What repairs have been done?"** — Compressor replacement under 3 years ago = red flag (underlying issue not fixed)
4. **"Have you had any refrigerant leaks?"** — Multiple leak repairs = system is near end of life
5. **"Is the system still under warranty?"** — Request the warranty certificate; many are non-transferable
6. **"What temperature do you keep it at?"** — 78°F is standard; anything below 74°F suggests a system that struggles to satisfy
7. **"Have you had any drainage issues?"** — Water damage near the air handler = past or present drain problem
8. **"When was the ductwork last inspected?"** — Ducts in Florida attics degrade every 10-15 years
9. **"Was a Manual J load calculation done for this system?"** — If not, the system may be incorrectly sized (most are)
10. **"Are all permits closed?"** — Unpermitted work is your liability after closing

## Red Flags That Justify a Professional AC Inspection

If you see any of these during your showing, make your offer contingent on a licensed [HVAC contractor](https://ac-repair.today/) performing a full system evaluation:

- Condenser coil corrosion visible through the grille
- Rust on the bottom of the condenser cabinet (standing water damage)
- Musty smell from the vents (mold in ducts or air handler)
- Visible water stains near the air handler
- System that runs continuously without reaching the set temperature
- Ice or frost on refrigerant lines at the outdoor unit
- Thermostat that's "programmed" to 82°F+ during the showing (masking poor performance)
- No permit history found for the installation date
- Air handler in the attic with no secondary drain pan or safety switch

## Estimated Remaining Life by System Age

| Age | Expected Remaining Life | Recommended Action |
|-----|------------------------|--------------------|
| 0-4 years | 12-16 years | Normal maintenance, verify transferable warranty |
| 5-8 years | 7-10 years | Professional inspection, budget for replacement in 5-7 years |
| 9-12 years | 3-6 years | Plan replacement within 2-3 years; negotiate credit |
| 13+ years | 0-3 years | Expect replacement immediately; negotiate full replacement cost |
| Unknown/no data | Assume worst | Factor full replacement into your offer |

The numbers above assume reasonable maintenance. A poorly maintained 6-year-old unit in coastal Miami can have less life remaining than a well-maintained 12-year-old unit inland.

## After Closing — First 90 Days

Once you own the home:
1. **Schedule a full AC maintenance visit** — a technician should clean coils, check refrigerant, test all safety controls, and inspect the ductwork. [Professional AC maintenance](https://ac-repair.today/services/ac-maintenance/) catches the issues a home inspection missed.
2. **Change the filter immediately** — you don't know when it was last changed
3. **Register the warranty** — many manufacturer warranties transfer to new owners within 30-60 days of closing, but only if you register
4. **Document everything** — take photos of the condenser model/serial, air handler model/serial, and any existing issues
5. **Learn the system** — find the electrical disconnect, the condensate drain exit, and the filter location before you need them in an emergency

## Summary

A home's AC system in South Florida is not an amenity — it's a critical infrastructure component that costs $6,000-12,000 to replace. A 15-minute visual inspection during a showing can catch 70% of serious problems before you make an offer. Combine that with the permit check and two or three specific questions to the seller, and you'll avoid the most expensive surprises.

When in doubt, bring in a licensed [HVAC contractor](https://ac-repair.today/services/ac-repair/) for a buyer's inspection. In South Florida's climate, the $150-200 inspection fee is the cheapest insurance you can buy.

---

*Created for South Florida home buyers. Professional AC inspections by [AC Repair Today](https://ac-repair.today) — serving Miami-Dade, Broward, and Palm Beach. FL License CAC1824118.*
