import os

root = "../../json/archive/risultati genetico"
for path, subdirs, files in os.walk(root):
    for name in files:
        if "results_serialized" in name:
            print os.path.join(path, name)

            # here I have all the directories with results