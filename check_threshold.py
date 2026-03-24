import sys

accuracy = 0.90 

print(f"--- Pipeline Quality Check ---")
print(f"Current Accuracy: {accuracy}")
print(f"Threshold Required: 0.85")

if accuracy < 0.85:
    print("RESULT: FAILED - Accuracy is below threshold!")
    sys.exit(1)
else:
    print("RESULT: SUCCESS - Accuracy meets requirements.")
    sys.exit(0)
