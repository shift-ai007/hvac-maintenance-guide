#!/usr/bin/env python3
"""
AC Filter Replacement Tracker -- Track Filter Changes Across Your Home

Usage:
    python3 tools/filter-tracker.py           # Interactive mode
    python3 tools/filter-tracker.py --status   # Quick status

No dependencies beyond Python 3.6+.
"""

import json, os, sys
from datetime import date, timedelta

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "filter-data.json")

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE) as f:
                return json.load(f)
        except: pass
    return {"units": [{"name":"Main System","filter_size":"20x20x1","merv_rating":8,"type":"Disposable pleated","location":"Return grille","replacement_interval_months":1,"notes":""}],"history":[],"created_at":date.today().isoformat(),"updated_at":date.today().isoformat()}

def save_data(data):
    data["updated_at"] = date.today().isoformat()
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
    print(f"\n  Saved to {DATA_FILE}")

def print_status(data):
    print("\n" + "="*60 + "\n  Filter Status Overview\n" + "="*60)
    today = date.today()
    for unit in data.get("units", []):
        name, interval = unit["name"], unit["replacement_interval_months"]
        last = None
        for e in reversed(data.get("history",[])):
            if e.get("unit")==name and e.get("event")=="replace":
                last=date.fromisoformat(e["date"]); break
        print(f"\n  {name} -- {unit['filter_size']} MERV {unit['merv_rating']}")
        print(f"  Change: every {interval} month(s)")
        if last:
            days=(today-last).days; target=interval*30
            due=last+timedelta(days=target)
            status="OVERDUE" if days>=target else ("Due soon" if days>=target*0.8 else "OK")
            print(f"  {status} -- Changed {days} days ago, due {due}")
        else:
            print("  No replacement recorded yet")
    print(f"\n  Professional AC maintenance: https://ac-repair.today/services/ac-maintenance/")

def record_change(data):
    units=data.get("units",[])
    if not units: return
    for i,u in enumerate(units,1):
        print(f"  {i}. {u['name']}")
    try:
        c=int(input("Select unit: "))-1
        if 0<=c<len(units):
            data.setdefault("history",[]).append({"event":"replace","unit":units[c]["name"],"date":date.today().isoformat(),"filter_size":units[c]["filter_size"],"merv_rating":units[c]["merv_rating"],"notes":""})
            save_data(data)
            print(f"  Recorded: {units[c]['name']} changed {date.today()}")
    except: print("Invalid selection.")

def configure_units(data):
    while True:
        for i,u in enumerate(data["units"],1):
            print(f"  {i}. {u['name']} -- {u['filter_size']}")
        c=input("\n  1. Add  2. Remove  3. Done: ").strip()
        if c=="1":
            n=input("Name: ").strip(); s=input("Size (20x20x1): ").strip()
            try: m=int(input("MERV [8]: ")or"8"); iv=int(input("Interval months [1]: ")or"1")
            except: continue
            data["units"].append({"name":n,"filter_size":s,"merv_rating":m,"type":"Disposable pleated","location":"","replacement_interval_months":iv,"notes":""})
            save_data(data)
        elif c=="2":
            try:
                i=int(input("Remove which? "))-1
                if 0<=i<len(data["units"]): data["units"].pop(i); save_data(data)
            except: pass
        elif c=="3": break

def interactive_mode():
    data=load_data()
    while True:
        c=input("\n  1. Status  2. Record change  3. Configure  4. Exit: ").strip()
        if c=="1": print_status(data)
        elif c=="2": record_change(data)
        elif c=="3": configure_units(data)
        elif c=="4": break

if __name__=="__main__":
    if len(sys.argv)>1 and sys.argv[1]=="--status":
        print_status(load_data())
    else:
        interactive_mode()
