import sys
accuracy = 0.90 

print("--- Accuracy Validation Check ---")
print(f"Model Accuracy: {accuracy}")

if accuracy >= 0.85:
    print("SUCCESS: Accuracy is above 0.85. Proceeding to Deployment...")
    # مفيش sys.exit(0) هنا، نسيب الـ script يخلص طبيعي
else:
    print("FAILED: Accuracy is too low!")
    sys.exit(1) # بنستخدم دي فقط في حالة الفشل
