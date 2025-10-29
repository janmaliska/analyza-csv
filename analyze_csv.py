#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to analyze automotive spare parts CSV and estimate 2026 sales.
"""

import csv
import re
from typing import Dict, List

# Define luxury car brands that typically have lower sales for non-original parts
LUXURY_BRANDS = {
    'BMW', 'MERCEDES-BENZ', 'AUDI', 'PORSCHE', 'JAGUAR', 'LAND ROVER',
    'LEXUS', 'VOLVO', 'ALFA ROMEO', 'MASERATI', 'BENTLEY', 'ROLLS-ROYCE'
}

# Define mainstream brands with higher sales potential
MAINSTREAM_BRANDS = {
    'ŠKODA', 'VOLKSWAGEN', 'FORD', 'OPEL', 'RENAULT', 'PEUGEOT', 'CITROËN',
    'HYUNDAI', 'KIA', 'TOYOTA', 'NISSAN', 'MAZDA', 'HONDA', 'DACIA', 'FIAT',
    'SEAT', 'SUZUKI', 'MITSUBISHI'
}


def extract_brand(car_type: str) -> str:
    """Extract car brand from the car type column."""
    if not car_type or car_type == '':
        return ''
    
    # The brand is before the first pipe separator
    parts = car_type.split('|')
    if len(parts) > 0:
        return parts[0].strip().upper()
    
    return ''


def estimate_sales(row: Dict[str, str]) -> int:
    """
    Estimate 2026 sales for a spare part based on various factors.
    
    Factors considered:
    - Number of registered cars on the market
    - Car brand (luxury vs mainstream)
    - Base assumption: non-original parts are replacement items
    """
    
    # Get number of registered cars
    try:
        registered_cars = int(row['Výskyt registrovaných aut na trhu'])
    except (ValueError, KeyError):
        registered_cars = 0
    
    # If no registered cars data, return 0
    if registered_cars == 0:
        return 0
    
    # Extract brand
    brand = extract_brand(row.get('Typ auta', ''))
    
    # Base calculation: estimate that a certain percentage of cars will need this part
    # Assumption: Parts like bumpers, absorbers have 2-5% annual replacement rate
    
    if registered_cars < 500:
        # Very few cars - minimal sales expected
        base_rate = 0.01  # 1%
    elif registered_cars < 2000:
        # Small market
        base_rate = 0.02  # 2%
    elif registered_cars < 5000:
        # Medium market
        base_rate = 0.025  # 2.5%
    elif registered_cars < 10000:
        # Large market
        base_rate = 0.03  # 3%
    else:
        # Very large market
        base_rate = 0.035  # 3.5%
    
    # Adjust for brand type
    if brand in LUXURY_BRANDS:
        # Luxury cars: owners more likely to buy original parts
        brand_multiplier = 0.4  # 40% market share for non-original parts
    elif brand in MAINSTREAM_BRANDS:
        # Mainstream brands: higher acceptance of non-original parts
        brand_multiplier = 0.8  # 80% market share for non-original parts
    else:
        # Unknown brand - use conservative estimate
        brand_multiplier = 0.6  # 60% market share
    
    # Calculate estimate
    estimated_units = registered_cars * base_rate * brand_multiplier
    
    # Round to nearest integer, minimum 1 if calculation suggests any sales
    if estimated_units < 1 and estimated_units > 0:
        return 1
    
    return round(estimated_units)


def process_csv(input_file: str, output_file: str):
    """
    Process the CSV file and add sales estimates.
    """
    
    rows_processed = 0
    
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile, delimiter=';')
        
        # Get existing fieldnames and add new column
        fieldnames = reader.fieldnames
        if not fieldnames:
            raise ValueError("No fieldnames found in CSV")
        
        fieldnames = list(fieldnames)
        fieldnames.append('Odhad prodeje 2026')
        
        # Write output file
        with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            
            for row in reader:
                # Estimate sales for this row
                estimated_sales = estimate_sales(row)
                row['Odhad prodeje 2026'] = str(estimated_sales)
                
                writer.writerow(row)
                rows_processed += 1
    
    print(f"✓ Zpracováno {rows_processed} položek")
    print(f"✓ Výstupní soubor uložen do: {output_file}")


if __name__ == '__main__':
    input_file = 'input/Pokus 1177 karet k vyhodnocení.csv'
    output_file = 'output/vyhodnoceni_2026.csv'
    
    print("Spouštím analýzu CSV souboru...")
    print(f"Vstupní soubor: {input_file}")
    
    process_csv(input_file, output_file)
    
    print("\nAnalýza dokončena!")
