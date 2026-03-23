import sys
accuracy = 0.90 # لو عايزاه ينجح خليها 0.90، لو عايزاه يفشل خليها 0.80
if accuracy < 0.85:
    print("Failed: Accuracy below threshold")
    sys.exit(1)
else:
    print("Success: Accuracy above threshold")
    sys.exit(0)
