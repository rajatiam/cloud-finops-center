import csv, hashlib, io, json, math, re
from datetime import datetime, timezone
from urllib.request import Request, urlopen
from .validation import validate_input, http_url, unique

def now(): return datetime.now(timezone.utc).isoformat()
def validate(data,records): return initialize(validate_input(data,CONFIG['example']),records)

from decimal import Decimal
def initialize(row,records): return row
def estimate(row): return Decimal(str(row['hourly_cost']))*Decimal(str(row['monthly_hours']))
def summary(rows):
    teams={}
    for row in rows: teams[row['team']]=teams.get(row['team'],Decimal('0'))+estimate(row)
    return {'monthly_estimate':float(round(sum((estimate(r) for r in rows),Decimal('0')),2)),'over_budget':sum(estimate(r)>Decimal(str(r['budget'])) for r in rows),'by_team':{team:float(round(value,2)) for team,value in teams.items()}}
def transition(row,action): raise ValueError('Estimates are immutable; create a revised estimate')
