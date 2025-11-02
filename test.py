import os, glob, pathlib

root = pathlib.Path("C:/Data/hboict/Sem7-AIFS/Personal_Project")
out = root / "labels"
out.mkdir(exist_ok=True)

def list_rel(subfolder):
    vids = []
    exts = ("*.mp4","*.mov","*.avi","*.mkv","*.MP4","*.MOV","*.AVI","*.MKV")
    for ext in exts:
        vids += glob.glob(str(root / subfolder / ext))
    vids = [str(pathlib.Path(v).relative_to(root)) for v in vids]
    vids.sort()
    return vids

correct = list_rel("Correct sequence")
incorrect = list_rel("Wrong sequence")

(out / "correct.txt").write_text("\n".join(correct) + "\n")
(out / "incorrect.txt").write_text("\n".join(incorrect) + "\n")

print("Wrote:", out / "correct.txt")
print("Wrote:", out / "incorrect.txt")
print(f"{len(correct)} correct, {len(incorrect)} incorrect")