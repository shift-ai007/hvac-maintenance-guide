# Smart Home AC Automation Guide — South Florida Edition

> A practical guide to reducing AC energy consumption using smart home technology in South Florida's unique climate.

## Overview

South Florida homeowners face the longest cooling season in the continental US — April through November with average temperatures of 85-95°F and humidity above 70%. This guide covers specific automation strategies proven to reduce AC energy consumption by 20-30%.

## Prerequisites

- A smart thermostat with geofencing and humidity control (Ecobee, Sensi, Nest, or Home Assistant compatible)
- Basic familiarity with your thermostat's companion app
- (Optional) Additional sensors for deeper automation

## 1. Geofencing Configuration

### Why It Matters in South Florida
The standard recommendation assumes your AC can rest. In South Florida, your AC runs 10-14 hours daily in peak summer. Even a few hours of reduced runtime compounds into significant savings.

### Setup Steps

**Ecobee:**
1. Open the Ecobee app → Main Menu → Home & Away
2. Enable "Smart Home & Away" and "Follow Me"
3. Set Away hold temperature to 82°F
4. Enable "Smart Recovery" (start cooling 30 min before arrival — critical in humid climates)

**Sensi:**
1. Open Sensi app → Settings → Smart Away
2. Enable geofencing for all household members
3. Set Away temperature to 84°F (Sensi's 2-stage cooling works well with this wider setback)

**Home Assistant:**
```yaml
# automation.yaml snippet
automation:
  - alias: "AC Away Mode"
    triggers:
      - platform: state
        entity_id: zone.home
        from: "home"
        to: "not_home"
    actions:
      - action: climate.set_temperature
        target:
          entity_id: climate.downstairs
        data:
          temperature: 83
```

### Expected Savings: $40-60/month during peak season

## 2. Humidity Priority Mode

### Why It Matters
South Florida's humidity makes 78°F at 90% humidity feel worse than 74°F at 50%. Humidity priority shifts the thermostat's target from temperature alone to a temperature+humidity blend.

### Enabling Humidity Control

**Ecobee:**
1. Main Menu → Settings → Installation Settings → Thresholds
2. Set "AC Overcool Max" to 2°F
3. Enable "Dehumidify with AC"
4. Set target humidity to 50%

**Manual thermostat:**
Most thermostats hide humidity priority in "contractor settings." Access with:
1. Press and hold the "Menu" button for 10 seconds
2. Navigate to "Dehumidification" or "Humidity Control"
3. Set to "On" with target 45-50%

### Expected Savings: 8-12% reduction on monthly cooling cost

## 3. FPL Time-of-Use Scheduling

### Why It Matters
FPL TOU rates charge significantly more from 4-9 PM weekdays. A smart scheduling strategy pre-cools during off-peak and lets the temperature drift during peak.

### Strategy
| Time | Thermostat Setting | Rationale |
|------|-------------------|-----------|
| 12-4 PM | 74°F (pre-cool) | Off-peak, store coolth |
| 4-9 PM | 80°F (drift) | Peak rates, minimal AC |
| 9 PM-6 AM | 76°F | Off-peak, sleeping comfort |
| 6 AM-12 PM | 78°F | Off-peak, nobody home |

### Expected Savings: 15-20% on total cooling bill with TOU plan

## 4. Advanced Automation (Home Assistant)

For those running Home Assistant, these automations compound savings further:

### Window Detection
```yaml
automation:
  - alias: "Pause AC on Open Window"
    triggers:
      - platform: state
        entity_id: binary_sensor.living_room_window
        to: "on"
    actions:
      - action: climate.set_hvac_mode
        target:
          entity_id: climate.downstairs
        data:
          hvac_mode: "off"
```

### Zone-Based Cooling
Use motion sensors in each zone to restrict cooling to occupied areas only. In multi-story homes, this alone cuts runtime by 25%.

### Filter Change Alerts
Track runtime hours and alert at 720 hours (30 days × 24h runtime in South Florida summer):
```yaml
template:
  - sensor:
      - name: "AC Runtime Monthly"
        unit_of_measurement: "h"
        state: >
          {{ states('sensor.ac_runtime_hours') | float }}
```

## 5. Maintenance Integration

Smart home automation detects efficiency drift — a 20% increase in daily runtime at the same outdoor temperature signals a problem. Common culprits:

- Dirty filter (costs 5-15% efficiency)
- Low refrigerant (costs 10-20% efficiency)
- Dirty condenser coil (costs 5-10% efficiency)

When you see this pattern, schedule a [professional AC maintenance visit](https://ac-repair.today/services/ac-maintenance/) or check for [emergency AC repair](https://ac-repair.today/services/emergency-ac-repair/) if the system is struggling to reach temperature.

## Ready to Upgrade?

If your current system is over 12 years old, consider a [modern high-efficiency AC installation](https://ac-repair.today/services/ac-installation/) with variable-speed technology. These systems natively support the fine-grained control that smart thermostats provide.

---

*Built and maintained by [AC Repair Today](https://ac-repair.today/) — South Florida's trusted HVAC provider. Licensed and insured.*
