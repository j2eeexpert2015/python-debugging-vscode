import os
import importlib.util
import sys

print("🔍 Verifying Python Project Setup...\n")

# Step 1: List valid Python packages (folders with __init__.py)
packages = [d for d in os.listdir() if os.path.isdir(d) and '__init__.py' in os.listdir(d)]
print("📦 Found local packages:", packages)

# Step 2: Check if 'util' package is importable
print("\n🧪 Checking if 'util' is importable...")

if importlib.util.find_spec("util"):
    print("✅ 'util' package is importable.")
else:
    print("❌ 'util' package is NOT found.")
    print("ℹ️  Make sure you opened the correct project folder in VS Code.")
    print("📁 You should open the folder that contains .vscode/settings.json as the workspace root.")

# Step 3: Show current working directory and sys.path[0]
print("\n📍 Current working directory:", os.getcwd())
print("🔧 sys.path[0]:", sys.path[0])
