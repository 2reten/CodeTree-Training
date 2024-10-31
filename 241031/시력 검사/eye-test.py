vision_r = float(input())
vision_l = float(input())

if vision_l >= 1.0 and vision_r >= 1.0:
    print("High")
elif vision_l >= 0.5 and vision_r >= 0.5:
    print("Middle")
else: print("Low")