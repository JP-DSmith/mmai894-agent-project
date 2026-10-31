import os
import json

DATA_DIR = "data/world_v1"

def test_world_files_exist():
    """Verify that all four core world v1 JSON files exist."""
    required_files = ["boots.json", "suppliers.json", "customers.json", "orders.json"]
    for filename in required_files:
        filepath = os.path.join(DATA_DIR, filename)
        assert os.path.exists(filepath), f"Missing required world file: {filename}"

def test_boots_data_structure():
    """Verify boots.json contains 10 styles with required attributes."""
    filepath = os.path.join(DATA_DIR, "boots.json")
    with open(filepath, "r") as f:
        boots = json.load(f)
    
    assert len(boots) == 10, f"Expected 10 boot styles, found {len(boots)}"
    for boot in boots:
        assert "boot_id" in boot
        assert "name" in boot
        assert "origin_country" in boot
        assert "cost_cad" in boot

def test_suppliers_customers_orders_not_empty():
    """Verify suppliers, customers, and orders datasets are populated."""
    for entity in ["suppliers.json", "customers.json", "orders.json"]:
        filepath = os.path.join(DATA_DIR, entity)
        with open(filepath, "r") as f:
            data = json.load(f)
        assert len(data) > 0, f"{entity} is empty!"
