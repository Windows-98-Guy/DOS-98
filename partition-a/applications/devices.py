import os

os.system("color 1f")
os.system("@Mode 50, 20")

print("""
==================== DEVICES =====================
[  FLOPPY DRIVE E:\            STATUS: INACTIVE  ]
[  LOCAL DRIVE A:\             STATUS: ACTIVE    ]
[  LOCAL DRIVE B:\             STATUS: ACTIVE    ]
[================================================]
[  LOCAL DRIVE A:\             NAME: partition-a ]
[  LOCAL DRIVE B:\             NAME: partition-b ]
[================================================]
[         Type in 'exit' to exit Devices         ]
[================================================]
""")

action = input(">>> ")
if 'exit' in action:
    os.close("devices.py")
else:
    pass