import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

CSV_FILE = "colors_dataset.csv"   # Make sure this file is in the same folder

# ----------------------------------
# Load Dataset
# ----------------------------------
df = pd.read_csv(CSV_FILE)

# Features and target
X = df[["R", "G", "B"]]
y = df["label"]

# ----------------------------------
# Train-Test Split (Supervised ML)
# ----------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ----------------------------------
# Train Model
# ----------------------------------
model = DecisionTreeClassifier(max_depth=5)
model.fit(X_train, y_train)

# ----------------------------------
# Evaluate Model
# ----------------------------------
preds = model.predict(X_test)
print("\nMODEL ACCURACY:", accuracy_score(y_test, preds))

# ----------------------------------
# User Input
# ----------------------------------
user_color = input("\nEnter a color name (example: red, blue-purple, yellow-green): ").strip().lower()

# Check if the color exists in dataset
if user_color not in df["name"].str.lower().values:
    print("Color not found! Please enter one of the defined primary, secondary, or tertiary colors.")
    print("\nAvailable colors:")
    for name in df["name"]:
        print("-", name)
    exit()

# Get the RGB values for this color
row = df[df["name"].str.lower() == user_color]
rgb = row[["R", "G", "B"]].values[0]

# Predict warm or cool
prediction = model.predict([rgb])[0]

print("\nColor:", user_color)
print("RGB:", tuple(rgb))
print("Predicted Temperature:", prediction.upper())
