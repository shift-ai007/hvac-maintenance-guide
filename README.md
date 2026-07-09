# HVAC Maintenance Guide

A comprehensive guide for homeowners to maintain their HVAC systems, troubleshoot common issues, and know when professional help is needed.

## Interactive Savings Calculator

Before diving into the guides, check how much you could save with better maintenance:

```bash
python3 tools/savings-calculator.py
```

This interactive tool estimates annual and long-term savings based on your system age, current habits, and local South Florida energy costs. [Try it now](tools/savings-calculator.py) — no dependencies needed.

## Interactive Maintenance Scheduler

Get a personalized year-round maintenance plan based on your system type, age, location, and last service dates:

```bash
python3 tools/maintenance-scheduler.py
```

The [maintenance scheduler](tools/maintenance-scheduler.py) generates a month-by-month calendar, priority action summary, and personalized tips for South Florida homeowners. Enter details about your system once and get a printable annual plan.

## AC Filter Tracker

Keep track of filter replacements across all your AC units:

```bash
python3 tools/filter-tracker.py           # Interactive mode
python3 tools/filter-tracker.py --status  # Quick status check
```

The [filter tracker](tools/filter-tracker.py) records every filter change, alerts you when replacements are due, maintains your filter sizes and MERV ratings, and tracks history. No dependencies — just Python 3.6+. Covers the MERV rating spectrum so you know exactly what to buy.

📖 New to filter selection? Read our **[complete AC filter buying guide](docs/ac-filter-guide.md)** — covers MERV ratings for South Florida homes, replacement schedules, where to buy, and the five costly mistakes to avoid.

## Why Maintenance Matters

- **Energy Savings**: A well-maintained system uses 15-25% less energy
- **Longevity**: Regular maintenance extends system life by 5-10 years
- **Air Quality**: Clean filters and ducts mean healthier indoor air
- **Cost Prevention**: $200/year in maintenance prevents $5,000+ emergency repairs

## Seasonal Maintenance Checklist

### Spring (Before Cooling Season)
- [ ] Replace air filter (or clean if reusable)
- [ ] Clean outdoor condenser coils
- [ ] Check refrigerant levels
- [ ] Test thermostat calibration
- [ ] Clear debris around outdoor unit (2ft clearance)
- [ ] Schedule professional [AC maintenance tune-up](https://ac-repair.today/services/ac-maintenance/)

### Fall (Before Heating Season)
- [ ] Replace air filter
- [ ] Inspect heat exchanger for cracks
- [ ] Test carbon monoxide detectors
- [ ] Check ductwork for leaks
- [ ] Clean condensate drain line

## Troubleshooting Common Issues

### AC Not Cooling
1. Check thermostat settings (cool mode, correct temp)
2. Replace dirty air filter
3. Check circuit breaker
4. Inspect outdoor unit for ice buildup
5. If none work → [Call for AC repair](https://ac-repair.today/services/ac-repair/)

### Uneven Temperatures
- Close vents in unused rooms
- Check for duct leaks
- Consider zone system installation
- Ensure proper insulation
- Professional [duct cleaning](https://ac-repair.today/services/duct-cleaning/) can restore airflow

### High Energy Bills
- Old system? Consider [AC replacement](https://ac-repair.today/services/ac-replacement/) — modern units are 30-50% more efficient
- Check duct insulation and sealing
- Upgrade to a programmable thermostat
- Schedule professional energy audit

## When to Call a Professional

**Emergency situations** requiring [immediate professional service](https://ac-repair.today/services/emergency-ac-repair/):
- Gas smell near furnace (evacuate first, call gas company)
- AC running but no cooling after basic troubleshooting
- Unusual noises (grinding, banging, squealing)
- Water leaking from indoor unit
- System won't turn on at all

## Upgrade Decisions

- [When to Replace Your AC System](docs/replacement-decision.md) — The 50% rule, age benchmarks, efficiency math, and rebate stacking for South Florida homeowners
- [Choosing and Using a Thermostat](docs/thermostat-guide.md) — Manual vs programmable vs smart, optimal schedules for South Florida, installation tips, humidity control
- [Heat Pump Guide for South Florida](docs/heat-pump-guide.md) — Can a heat pump work in our climate? Energy savings, configurations, specs to look for, and tax credits. A practical guide for homeowners considering the switch.

## Humidity & Air Quality

South Florida's humidity is a bigger comfort and health factor than most homeowners realize. Your AC system is your primary dehumidifier — learn how it works and when you need more:

- [Humidity Control for South Florida Homes](docs/humidity-control.md) — Why your AC may not be dehumidifying enough, whole-house dehumidifiers, air sealing, and monitoring
- [When and Why to Clean Your Air Ducts](docs/duct-cleaning-guide.md) — Signs your ducts need attention, what professional cleaning involves, costs, and how to choose a contractor
- [Mold Prevention in HVAC Systems](docs/mold-prevention-guide.md) — How mold forms in your AC, where it hides, and practical prevention steps every South Florida homeowner should take

- **[Whole-House Dehumidifier Integration Guide](docs/whole-house-dehumidifier-guide.md)** — When a standalone dehumidifier makes sense over portables, how it integrates with your ductwork, sizing for South Florida homes, and the monthly maintenance that keeps it working. Includes installation best practices for our humid climate.
- **[Whole-House Dehumidifier Maintenance Guide](docs/whole-house-dehumidifier-maintenance.md)** — Keeping your dehumidifier running efficiently year-round: monthly/seasonal/annual maintenance tasks, coil and drain cleaning, humidistat testing, corrosion checks, and troubleshooting common problems in South Florida's demanding humidity environment.

- **[Summer Indoor Air Quality Guide](docs/summer-indoor-air-quality-guide.md)** — A complete walkthrough of why IAQ drops during South Florida summers specifically: the interaction of humidity, closed-house conditions, continuous AC runtime, pollen, and VOCs. Includes a decision framework for identifying the right fix, a summer-specific maintenance calendar, and guidance on when professional help is needed.

Beyond dehumidification, learn about [indoor air quality solutions](https://ac-repair.today/services/indoor-air-quality/) including UV purifiers, HEPA filtration, and whole-home ventilation systems.

- **[The AC Filter: Your First Line of Defense](docs/ac-filter-iaq-efficiency-guide.md)** — MERV ratings explained for South Florida, the optimal filter change schedule for our climate, and how the right filter can save $200-500/year in prevented service calls and reduced energy waste.

## Coil Cleaning & Air Quality

Your evaporator and condenser coils are the heart of your AC system. When they're dirty, nothing works right:

- [Evaporator Coil Cleaning Guide](docs/evaporator-coil-cleaning.md) — How and when to clean the indoor coil, what to avoid, and when to call a pro. Essential reading for South Florida homeowners.
- [Dirty Sock Syndrome](docs/dirty-sock-syndrome.md) — That musty smell from your vents has a name. Learn what causes it, which fixes actually work, and why bleach makes it worse.
- [Condensate Drain Maintenance](docs/condensate-drain-maintenance.md) — The single most common AC service call in South Florida, explained. A $3 vinegar flush every 3 months can save you from a flooded ceiling.

## Summer Peak Load Management

Before the energy savings guide, consider this: most breakdowns happen not because the system is worn out, but because it enters summer with a small pre-existing issue that becomes a failure under peak load. Understanding the physics of why systems fail in June is the first step to preventing it.

- **[Peak Summer Load Management](docs/summer-peak-load-management.md)** — Why your AC struggles when temperatures hit 94°F, the three failure modes that emerge in June (capacitor degradation, airflow restriction feedback loops, marginal refrigerant charge), and the three-tier response framework that separates a working summer from an emergency-call summer. Includes measurable diagnostics homeowners can use before calling for [professional AC maintenance](https://ac-repair.today/services/ac-maintenance/).
- **[Summer Peak Performance Diagnostics](docs/summer-peak-performance-diagnostics.md)** — The measurable metrics that reveal your AC's true health during peak cooling season: temperature split (delta T), static pressure, compressor amp draw, and visual coil/line inspections. Includes a diagnostic quick-reference table and specific red-flag thresholds that indicate a system needs [professional attention](https://ac-repair.today/services/emergency-ac-repair/) before it fails. Written for homeowners who want data, not guesses.

## Whole-Home Cooling Strategy

Your AC doesn't work alone. Coordinating ceiling fans, window coverings, and thermostat programming can cut cooling costs by 20-35% while improving comfort.

- **[Whole-Home Cooling Strategy Guide](docs/whole-home-cooling-strategy.md)** — Combines four phases
- **[Whole-House HVAC Zoning Maintenance Guide](docs/whole-house-hvac-zoning-maintenance.md)** — How zoned systems work, monthly/quarterly damper checks, bypass duct testing, zone panel diagnostics, condensation prevention in humid climates, and energy-saving day/night scheduling strategies for South Florida homes. Includes when to call a [professional AC maintenance](https://ac-repair.today/services/ac-maintenance/) technician for static pressure balancing and limit switch calibration.: window management (solar screens, reflective film, cellular shades), ceiling fan sizing and scheduling, smart thermostat coordination, and passive measures (attic radiant barriers, insulation, exterior shading). Includes room-by-room guidance and expected combined savings. For [professional AC maintenance and whole-home assessments](https://ac-repair.today/services/ac-maintenance/), our licensed technicians serve all of South Florida.

## Summer Energy Savings Guide

New for 2026: A dedicated [summer energy savings guide](docs/summer-energy-savings-guide.md) for South Florida homeowners. Covers coil cleaning, duct sealing, thermostat optimization, and refrigerant checks — five proven ways to cut cooling costs by 20-40% without replacing your unit.

## Smart Thermostat Guide
>For a deeper technical breakdown of peak-summer efficiency strategies — including duct leakage remediation targets, thermostat setback curves, solar heat gain coefficients, and ceiling fan integration specs — see the [advanced summer energy savings reference](docs/summer-energy-savings-guide-advanced.md).

Modern [thermostat installation](https://ac-repair.today/services/thermostat-installation/) can save 10-15% on energy bills with features like learning schedules, geofencing, and remote control. For a deep dive on maximizing savings during our hottest months, see our new **[Smart Thermostat Strategies for Summer Energy Savings](docs/smart-thermostat-summer-strategies.md)** — covers peak-hour scheduling, fan circulation hacks, location-based schedules, and humidity management for South Florida's unique climate.

### Thermostat Wiring & Installation

About to swap out your old thermostat? Before you pull that faceplate, understand what those colored wires actually do and why the C-wire keeps causing headaches. Whether you're installing a basic programmable unit or a Wi-Fi smart thermostat, the wiring fundamentals are the same.

- **[Thermostat Wiring & Installation Basics](docs/thermostat-wiring-and-installation-basics.md)** — Complete wire color reference for South Florida systems (heat pump, straight cool, two-stage), step-by-step installation instructions, C-wire solutions, communicating system gotchas, and troubleshooting common installation issues. Written for homeowners who want to get it right the first time.
- **[Smart Thermostat Installation Compatibility Guide](docs/smart-thermostat-installation-compatibility.md)** — Compatibility checks (system type, C-wire, voltage), wiring diagrams with South Florida-specific gotchas (salt-air corrosion, 4-conductor wire, heat pump reversing valves), coastal installation considerations, and when a professional [thermostat installation service](https://ac-repair.today/services/thermostat-installation/) is the smarter choice.

## Smart HVAC Monitoring & IoT

Modern sensor technology lets you monitor your AC's health from your phone — catching problems like dirty filters, failing capacitors, and refrigerant leaks days or weeks before they cause a breakdown. For South Florida homes running AC 8-10 months a year, this can prevent most emergency repairs.

- **[Smart HVAC Monitoring & IoT Guide](docs/smart-hvac-monitoring-iot.md)** — What to monitor (temperature differential, runtime cycles, humidity, energy consumption), budget-to-enthusiast equipment recommendations ($0-500), critical vs. warning alert thresholds, and what to do when monitoring detects a problem. Covers why temperature differential trending is the single most powerful diagnostic you can do without a technician, how to set up push alerts, and which $15 sensor can save you from a $5,000 compressor replacement.

## Outdoor Spaces & Special Structures

South Florida homes often include unique spaces that standard HVAC guides don't cover. Two underserved areas:

- **[AC for Pool Equipment Rooms](docs/pool-equipment-hvac.md)** — How salt air, heat, and humidity destroy your pool pump, control boards, and gas heater — and what to do about it. Ventilation requirements, condensate management, and coastal corrosion protection for pool house enclosures.

- **[Outdoor Kitchen & Patio Cooling](docs/outdoor-kitchen-hvac.md)** — Mini-split installation, sizing, and operation tips for covered patios, lanais, and outdoor kitchens. Humidity management, placement considerations, and when mini-splits won't work.

## Refrigerant Awareness

Every AC system operates on a sealed refrigerant loop. Knowing how it works — and spotting problems early — can save your compressor and thousands in repair costs.

- **[Refrigerant: What Homeowners Should Know](docs/refrigerant-maintenance-safety.md)** — How refrigerant works, leak signs, refrigerant types timeline, when the economics favor replacement, and the five maintenance habits that protect your system's sealed loop. Essential reading before calling a technician.

## Compressor Care & Airflow Performance

Two aspects of HVAC maintenance that homeowners often overlook:

- **[Airflow Balancing Guide](docs/airflow-balancing.md)** — How to diagnose and fix hot and cold spots throughout your home. Covers hand tests, temperature splits, return air paths, and when to call a pro. Essential reading for South Florida's open-plan and closed-bedroom layouts.

- **[AC Compressor Maintenance](docs/ac-compressor-maintenance.md)** — Salt air, thunderstorms, and heat stress make South Florida uniquely hard on compressors. Learn the five maintenance practices that can extend compressor life from 10 years to 18+ years, plus early warning signs of trouble and what to do about them.

## Frozen Coils & Emergency Issues

Ice on your evaporator coil is one of the most common — and most misunderstood — AC problems in South Florida. Catching it early can save your compressor.

- **[Frozen Evaporator Coil Guide](docs/frozen-evaporator-coil.md)** — Why coils freeze in 95°F weather, how to tell airflow problems from refrigerant leaks, emergency thawing steps, and the $5 monthly fix that prevents 90% of freeze-related service calls. Essential reading before calling for [emergency AC repair](https://ac-repair.today/services/emergency-ac-repair/).

## Short Cycling — Why Your AC Runs in Bursts

If your AC turns on and off every few minutes, it's short cycling — and it's damaging your compressor and wasting energy. South Florida's combination of oversized systems, humidity, and salt air makes this one of the most common problems in our region.

- **[AC Short Cycling Guide](docs/ac-short-cycling.md)** — The three causes of short cycling, how to diagnose which one you have, and when it's a DIY fix vs a call for professional [AC repair](https://ac-repair.today/services/ac-repair/). Includes a diagnostic flowchart and prevention checklist.

## Electrical Protection

South Florida's thunderstorm season means every AC system is at risk from voltage surges and lightning damage — a risk many homeowners don't consider until it's too late:

- **[AC Surge Protection & Lightning Damage Guide](docs/ac-surge-protection.md)** — How surges damage your AC's contactor, control board, capacitor, and compressor; whole-home vs point-of-use protection; early warning signs of surge damage; what to do after a near strike; and how to navigate insurance claims. Essential reading before hurricane season.

For professional diagnosis and [AC repair](https://ac-repair.today/services/ac-repair/) after storm damage, our licensed technicians serve all of South Florida.

## AC Running Non-Stop — Why It Happens

If your AC runs for hours without shutting off (especially during South Florida's 95°F+ summer afternoons), it's either working as designed or signaling a problem. The line between normal and "needs repair" depends on runtime length, temperature differential, and whether it ever cycles off.

- **[Why Your AC Runs Non-Stop in Summer](docs/ac-running-nonstop-summer-causes.md)** — The 7 root causes ranked by likelihood: undersized systems, dirty filters, low refrigerant, dirty evaporator coils, thermostat issues, return air restrictions, and leaky ductwork. Includes a diagnostic decision table for DIY vs calling a pro, a runtime measurement protocol homeowners can use, and South Florida-specific guidance for each issue. Covers the critical difference between peak-day extended cycles and a system that genuinely won't satisfy the thermostat.

For immediate service when your AC won't stop running — or any [emergency AC repair in Miami](https://ac-repair.today/services/emergency-ac-repair/) — our technicians are on call 24/7 across all of South Florida.

## Electrical Contactors & Starting Components

The electrical contactor and run/start capacitors are the most common point of failure in South Florida AC systems — the combination of heat, humidity, and salt air accelerates corrosion and pitting on these components faster than in any other climate in the country. An annual inspection can prevent the most common "AC won't start" emergency.

- **[AC Contactor & Start Components Maintenance Guide](docs/ac-contactor-start-components.md)** — How the contactor, run capacitor, start capacitor, and potential relay work; visual inspection checklists (pitting, bulging, corrosion); lifespan estimates for coastal vs inland homes; safe DIY visual checks vs what requires a licensed [AC repair](https://ac-repair.today/services/ac-repair/) technician; and surge protection recommendations for Florida's thunderstorm-prone grid. Essential pre-summer reading for every South Florida homeowner.

## Coastal Corrosion Prevention

If you live within 5 miles of a South Florida coastline, salt air is silently damaging your AC system every day — and most homeowners don't realize it until a coil fails or a compressor locks up in the middle of summer.

- **[Coastal Corrosion Prevention Guide](docs/coastal-corrosion-prevention.md)** — How salt air destroys outdoor units, which components fail first (condenser coils, electrical terminals, fasteners), and four prevention strategies ranging from monthly hose rinses to factory-coated coils. Includes a quarterly inspection checklist and when replacement beats continued repair.

For a professional assessment of corrosion damage in Miami-Dade or Broward, our licensed [AC repair technicians](https://ac-repair.today/services/ac-repair/) can evaluate whether a coil cleaning, coating, or replacement is the right call.

## Duct Insulation Guide

Your duct system carries cooled air through some of the hottest spaces in your home — unconditioned attics that can reach 140°F on a South Florida summer afternoon. Poorly insulated ducts waste 20-30% of your cooling energy and can cause condensation, mold, and ceiling stains.

- **[Duct Insulation Guide for South Florida](docs/duct-insulation-guide.md)** — R-value recommendations for our climate, condensation prevention, material comparisons (fiberglass vs foam vs spray), cost vs savings analysis, and how to check whether your current insulation is adequate. Essential reading before summer.

- **[Complete Ductwork Maintenance Guide](docs/hvac-ductwork-maintenance-guide.md)** — The full picture: how to inspect accessible ductwork for leaks, condensation, and pest damage, DIY leak detection methods (smoke test, pressure test, tissue test), when sealing is DIY vs pro, and a seasonal maintenance schedule. Written for South Florida homes where ducts run through 140°F attics and humid crawlspaces. [Professional duct inspection available](https://ac-repair.today/services/duct-cleaning/).

## Thermostat Calibration & Sensor Placement

Your thermostat is the brain of your HVAC system — but in South Florida's humid climate, sensor drift and poor placement can silently increase your energy bill by 15-30%. An uncalibrated thermostat that reads 2°F low keeps your compressor running an extra 30-60 minutes per cycle.

- **[Thermostat Calibration & Sensor Placement Guide](docs/thermostat-calibration-sensor-placement.md)** — How to verify your thermostat reads true, the 5-foot placement rule, where NOT to put a sensor (sunlight, supply vents, above electronics), seasonal calibration checklist for Florida homes, and when a professional relocation is the real fix.

For professional [AC maintenance](https://ac-repair.today/services/ac-maintenance/) and thermostat installation, our licensed technicians can optimize your entire system.

## Hurricane Season Preparedness

June marks the start of Atlantic hurricane season, and your AC system is one of the most exposed parts of your home. A few hours of prep can save your compressor and keep you cool through recovery.

- **[Post-Hurricane AC Recovery Guide](docs/post-hurricane-recovery.md)** — The systematic restart sequence after a storm, generator compatibility, flood damage warning signs, and a preparation checklist for next season. Essential reading for every South Florida homeowner.
- **[Post-Hurricane Indoor Air Quality Guide](docs/post-hurricane-iaq-guide.md)** — The quiet threat after every storm: how elevated humidity, mold growth in water-damaged materials, and demolition particulates degrade your indoor air. Practical steps for drying, filtration, and knowing when to call a pro for [duct cleaning and IAQ assessment](https://ac-repair.today/services/duct-cleaning/).
- **[Wind-Driven Rain Protection for Outdoor AC Units](docs/wind-driven-rain-protection.md)** — How horizontal rain during storms infiltrates condensers, accelerates corrosion, and shorts equipment life. Covers enclosure options that don't block airflow, coastal-zone hardening tiers from shoreline to inland, the condensate drain connection after heavy weather, and post-storm signage that tells you whether [emergency AC repair](https://ac-repair.today/services/emergency-ac-repair/) is needed. Includes a hurricane-watch-to-post-storm preparation sequence specific to South Florida.

For storm-related [emergency AC repair in South Florida](https://ac-repair.today/services/emergency-ac-repair/), our team provides same-day service after major weather events.

## AC Condensate Water Reuse

Your AC doesn't just cool your home — it pulls 10–20 gallons of nearly distilled water from the air every day during South Florida's humid summer months. Most homes simply dump this valuable resource down the drain. Learn how to capture and reuse it for irrigation and outdoor use, saving $50–150 per year on water bills while reducing stormwater runoff.

- **[AC Condensate Water Reuse Guide](docs/ac-condensate-water-reuse-guide.md)** — How much condensate your AC produces by system size (5–30 gal/day depending on tonnage), collection methods from a $30 barrel setup to a full greywater integration, what you can and cannot safely use condensate for, mosquito management requirements (critical for South Florida), seasonal production patterns (wet vs dry season), and when to have a [professional AC maintenance technician](https://ac-repair.today/services/ac-maintenance/) modify your drain line for safe collection. Includes a common problems troubleshooting table and code considerations for Florida homeowners.

## Ductless Mini-Split Maintenance

Mini-splits are everywhere in South Florida — garages, additions, sunrooms, ADUs, and condos where ductwork can't go. They're efficient and quiet, but the indoor head pulls humid air across a cold coil all day, making it a magnet for biofilm, mold, and that musty "dirty sock" smell if it isn't cleaned properly.

- **[Ductless Mini-Split Maintenance Guide](docs/ductless-mini-split-maintenance.md)** — The monthly homeowner routine (filters, louvers, condensate), why the blower wheel needs an annual professional bib wash, coastal corrosion and condensate concerns unique to our climate, and the warning signs that mean it's time to call a pro. Includes a quick-reference maintenance schedule.

For professional mini-split cleaning, charge verification, and repair, our licensed [AC maintenance](https://ac-repair.today/services/ac-maintenance/) technicians service ductless systems alongside central AC across Miami-Dade, Broward, and Palm Beach.

## UV Germicidal Light Maintenance

UV-C germicidal lamps are a popular indoor-air-quality upgrade in our humid climate, but they fail silently — a lamp keeps glowing a faint blue long after it has stopped emitting the wavelength that actually kills mold and bacteria. Most coil lamps drop below useful output in about a year of continuous South Florida runtime.

- **[UV Germicidal Light Maintenance Guide](docs/uv-germicidal-light-maintenance.md)** — How UV-C lamps work, why a glowing lamp isn't necessarily a working lamp, the annual replacement routine, why our climate shortens lamp life, and the warning signs that the germicidal protection has lapsed. Includes a quick-reference schedule.

For a professional indoor-air-quality assessment, lamp replacement, and coil cleaning, our licensed [indoor air quality](https://ac-repair.today/services/indoor-air-quality/) technicians service Miami-Dade, Broward, and Palm Beach.

## Indoor Air Handler Maintenance

Your air handler — the indoor unit containing the evaporator coil, blower, and drain pan — runs every time your AC does. In South Florida's humid climate, it works harder than in any other region, making regular attention essential for reliable cooling.

- **[Indoor Air Handler Maintenance Guide](docs/air-handler-maintenance.md)** — What's inside your air handler (evaporator coil, blower motor, condensate drain pan, emergency float switch), the monthly maintenance checklist that prevents the most common emergency calls, how to spot the warning signs of a failing air handler before it leaves you without AC, and when a professional inspection is the right move. Essential reading before summer hits.

- **[Attic Air Handler Maintenance in South Florida](docs/attic-ac-unit-maintenance.md)** — The unique failure modes of attic-mounted equipment in our climate: heat-shortened capacitor life, rusted secondary drain pans that silently drip through ceilings, insulation-gasket leaks around blower-access doors, and the single cheapest $60 insurance device every attic system should have. Covers the annual attic checklist, warning signs (whistling, ceiling stains, musty smells below the unit), and when a float-switch install is better than a drywall repair.

For professional [AC maintenance](https://ac-repair.today/services/ac-maintenance/) that includes a full air handler inspection — blower evaluation, drain line clearing, coil check, and safety controls verification — our licensed technicians serve all of South Florida.

## Return Air & Static Pressure

The air your system delivers gets all the attention, but the air it has to pull *back in* is just as important. Undersized or restricted return air is one of the most overlooked causes of weak airflow, uneven cooling, and high bills in South Florida homes.

- **[Return Air & Static Pressure Guide](docs/return-air-and-static-pressure.md)** — What static pressure is and why most homes run too high, the local factors that starve returns (oversized equipment, dense filters, closed doors, crushed flex duct), the warning signs you can spot without tools, simple fixes you can try, and where the professional line is. Includes a quick-reference table.

For a system that whistles, freezes, or never quite cools evenly, our technicians measure static pressure as part of routine [professional AC maintenance](https://ac-repair.today/services/ac-maintenance/) across Miami-Dade, Broward, and Palm Beach.

## Blower Wheel Cleaning

Everyone changes the filter; almost no one cleans the blower wheel behind it. In humid climates that squirrel-cage fan cakes with dust and biofilm, quietly choking your airflow and raising your bill.

- **[Cleaning the Indoor Blower Wheel](docs/blower-wheel-cleaning.md)** — What the wheel does, the signs it's fouled, how it gets cleaned properly (and why high pressure ruins it), and when to bundle it into a tune-up. Catching this early is exactly what [professional AC maintenance](https://ac-repair.today/services/ac-maintenance/) is for.

## Refrigerant Lineset Insulation

That black foam on the copper line running into your house has one job: keep the cold suction line cold. In the South Florida sun it cracks, bleaches, and crumbles years early — then your system loses capacity and the bare pipe sweats into the wall.

- **[Refrigerant Lineset Insulation Maintenance](docs/lineset-insulation-maintenance.md)** — What the insulation does, how to spot UV failure without tools, why our climate destroys foam early, the simple re-insulation fix (and the UV-protection step everyone skips), and when corrosion means it's a repair job. A quick check that belongs in every [professional AC maintenance](https://ac-repair.today/services/ac-maintenance/) routine.

## Fresh Air Intake & ERV/HRV Maintenance

As South Florida homes get tighter and more energy-efficient, mechanical fresh-air ventilation — Energy Recovery Ventilators (ERVs) and Heat Recovery Ventilators (HRVs) — is becoming a standard upgrade. These systems bring filtered outdoor air in while recovering the cool you've already paid for, but they are not maintenance-free.

- **[Fresh Air Intake & ERV/HRV Maintenance](docs/fresh-air-intake-erv-hrv-maintenance.md)** — ERV vs HRV for South Florida's humid climate, the quarterly filter schedule and core cleaning steps that keep ventilation effective, the condensate drain that clogs just like your AC's, and when a failing ERV quietly stops ventilating while the fan keeps running. Includes signs that your unit needs a professional inspection.

## Attic Ventilation & Cooling Performance

Your attic isn't just storage space — it's the single biggest factor in how hard your AC has to work. An unventilated South Florida attic can hit 150°F, cooking your ductwork and adding 20-30% to your cooling load.

- **[Attic Ventilation and Your AC](docs/attic-ventilation-cooling.md)** — How a hot attic fights your air conditioner, the two types of attic ventilation (passive vs. powered), the insulation levels that actually make a difference in our climate, and when poor attic performance explains why your AC can't keep up despite regular maintenance.

## Summer Power Outage AC Protection

South Florida's severe thunderstorm and hurricane season brings frequent power outages that can silently damage AC compressors, capacitors, and control boards. Most homeowners don't realize their system is at risk until it's too late.

- **[Summer Power Outage AC Protection Guide](docs/summer-power-outage-ac-protection.md)** — What happens to your AC when the power goes out (voltage spikes on restore, short cycling from unequalized refrigerant pressures, brownout compressor overheating), the $200–400 whole-home surge protector fix that prevents most post-storm failures, the critical 5-minute wait rule before restarting your system, a symptom-to-likely-cause table for post-outage AC problems, and when "it was working fine before the storm" means an [emergency AC repair](https://ac-repair.today/services/emergency-ac-repair/) is needed.

## Summer Vacation AC Settings for Florida Homeowners

Planning a trip during South Florida's sweltering summer? What you do with your thermostat before you leave determines whether you come home to comfortable air conditioning — or a mold-infested, humidity-damaged disaster. Turning the AC completely OFF may save $40 in electricity, but it can cost thousands in remediation when indoor humidity hits 80%+ within 24 hours in our climate.

- **[Summer Vacation AC Settings for Florida Homeowners](docs/summer-vacation-ac-settings-florida.md)** — The 80–82°F sweet spot that balances energy savings with mold prevention, why Fan AUTO (not ON) is critical for moisture control in an unoccupied home, smart thermostat vacation mode features that alert you if the AC fails mid-trip, a complete pre-departure and post-return checklist tailored to South Florida, what happens when a thunderstorm knocks out power while you're away, and why an [AC maintenance checkup](https://ac-repair.today/services/ac-maintenance/) before vacation can prevent mid-trip failures.

## Humidity Setpoint Optimization

Most South Florida homeowners think about temperature when setting their thermostat, but humidity is the more important variable for comfort and efficiency from June through September.

- **[Humidity Setpoint Optimization Guide](docs/humidity-setpoint-optimization-summer.md)** — Why 76°F at 48% RH feels more comfortable than 74°F at 60% RH, the optimal summer setpoint strategy for our climate, how Fan AUTO vs ON changes indoor moisture by 5–10 percentage points, the "overcool to dehumidify" smart-thermostat feature that works brilliantly in South Florida, and when oversized equipment means no thermostat setting can fix the humidity problem. Includes [professional AC maintenance](https://ac-repair.today/services/ac-maintenance/) tips for verifying your system is performing both sensible and latent cooling correctly.

## Pet Owner's Guide to HVAC Maintenance

Pets and South Florida's year-round cooling season create unique maintenance demands. The combination of pet dander, fur, and high humidity loads filters 2-3× faster than standard recommendations assume, and pet-related drain blockages are among the most common preventable service calls in our region.

- **[Pet Owner's Guide to HVAC Maintenance](docs/pet-owner-hvac-maintenance.md)** — How pet dander and fur accelerate filter loading in South Florida homes, the biofilm that forms on evaporator coils from dander + condensate moisture, condensate drain blockages from pet hair, why pets left alone during peak heat days are at risk if the AC fails, outdoor unit corrosion from pet traffic, and a maintenance schedule tailored to pet households.

## Outdoor Unit Landscaping & Clearance

South Florida's fast-growing tropical vegetation is one of the most common — and most overlooked — causes of premature AC failure. A hedge that provides proper clearance in March will be pressing against the condenser cabinet by June.

- **[Outdoor Unit Landscaping & Clearance Guide](docs/outdoor-unit-landscaping-clearance.md)** — The manufacturer clearance minimums and why South Florida's climate demands more, plants to avoid near the condenser and safe alternatives, the seasonal pre-hurricane and post-storm inspection checklist, how restricted airflow silently damages compressors over years, and when chronic high head pressure from vegetation encroachment requires an [emergency AC repair](https://ac-repair.today/services/emergency-ac-repair/).

## AC Noise & Vibration Diagnosis

South Florida's year-round cooling season means AC components wear 2–3× faster than in northern climates. Knowing which sounds signal trouble and which are normal can prevent small issues from becoming expensive emergency repairs.

- **[AC Noise & Vibration Diagnosis Guide](docs/ac-noise-vibration-diagnosis.md)** — What each common AC sound means (buzzing contactor, squealing fan bearings, rattling panels, hissing refrigerant, gurgling drains), the monthly 60-second listening walk that catches problems early, a symptom-to-action reference table, and when a sound you've never heard before means it's time to call for [emergency AC repair](https://ac-repair.today/services/emergency-ac-repair/). Includes practical checks you can do yourself and guidance on when an [AC maintenance visit](https://ac-repair.today/services/ac-maintenance/) is the most cost-effective fix.

## AC Warranty Guide for Florida Homeowners

Understanding your AC warranty can save you thousands — but Florida's coastal environment, registration requirements, and maintenance stipulations create pitfalls that catch most homeowners off guard. Many manufacturers reduce 10-year warranties to 5 years if the system isn't registered within 60 days, and salt-air corrosion is often explicitly excluded from coverage.

- **[AC Warranty Guide for Florida](docs/ac-warranty-guide-florida.md)** — The full breakdown of manufacturer equipment warranties, installer labor warranties, and extended service plans; how coastal corrosion voids coverage and what to do about it; registration deadlines for every major brand; the maintenance documentation you need to keep claims valid; and a decision framework for when to file a warranty claim versus when to replace. Includes practical tips on transferring warranties when buying a home.

## Special Situations

### Home Renovation & Construction HVAC Protection

If you are renovating your South Florida home, your AC system is at risk from drywall dust, sawdust, and construction debris. A few basic precautions can prevent costly damage that often does not show up until weeks after the contractors leave.

- **[Construction & Renovation HVAC Protection Guide](docs/construction-renovation-hvac-protection.md)** — How to protect your system before, during, and after construction: sealing registers during dusty work, the aggressive filter-change schedule (every 3–4 days) during active renovation, the post-project restoration sequence (filter flush, coil inspection, blower wheel check, performance verification), and when a professional [AC maintenance visit](https://ac-repair.today/services/ac-maintenance/) after construction is the smartest investment you can make. Includes a complete pre-renovation checklist and contractor liability documentation guidance for Florida homeowners.

### Vacation Home & Seasonal AC Management

South Florida's snowbird and seasonal property owners face unique AC challenges: a system that sits idle for months in the region's punishing humidity can develop mold, drain clogs, and compressor damage — while one that is left at the wrong temperature setting can cost thousands in restoration.

- **[Seasonal & Vacation Home AC Management Guide](docs/vacation-home-snowbird-ac-care.md)** — The correct thermostat settings for short absences (1–7 days) versus long seasonal closures (3+ months), why the "85°F rule" creates mold risk in South Florida, the pre-departure checklist (filter, drain flush, float switch test, outdoor clearance, disconnect considerations), the gradual pull-down procedure when returning, and what to do if the system fails while you are away. Covers rental property between-tenant maintenance and hurricane-season considerations for seasonal homeowners.

## Home Buyer & New Homeowner Guides

If you're buying a home in South Florida or just moved into a new construction house, the AC system can hide expensive surprises.

- **[Home Buyer's AC Inspection Checklist](docs/home-buyer-ac-inspection-checklist.md)** — What every South Florida home buyer needs to check before closing: permit history verification, condenser coil condition beyond a surface look, the 20-minute runtime test that reveals hidden problems, the 10 questions to ask the seller, and when to make an offer contingent on a professional evaluation. Includes a Python delta-T calculator and red-flag thresholds for every major AC component. Licensed [AC inspections](https://ac-repair.today/services/ac-repair/) available in Miami-Dade, Broward, and Palm Beach.

## Energy Monitoring

Your AC is your home's biggest energy user — but without monitoring, you never see the gradual efficiency loss that quietly adds $50–100 to monthly bills. A $15 smart plug or $80 circuit monitor can detect failing capacitors, dirty coils, and refrigerant leaks days or weeks before they cause a breakdown.

- **[Energy Monitoring: Smart Plugs & Whole-Home Systems](docs/energy-monitoring-smart-plugs-and-whole-home.md)** — How to use smart plugs, circuit-level monitors (Emporia Vue, Sense, IotaWatt), and smart thermostat reports to track your AC's power consumption. Covers diagnostic patterns for each failure mode, temperature-dependent alert thresholds, recommended setups from $15 to $350, and the exact amp-draw signatures that tell you whether you need [AC maintenance](https://ac-repair.today/services/ac-maintenance/) vs [emergency AC repair](https://ac-repair.today/services/emergency-ac-repair/). Written specifically for South Florida homeowners running AC 8–10 months a year.

## About

Created by HVAC professionals at [AC Repair Today](https://ac-repair.today/) — serving homeowners with honest, reliable HVAC service.

## License

CC BY 4.0
