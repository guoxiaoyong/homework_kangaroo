import json
import glob

all_files = glob.glob('*.mp4')

result = []
for fn in all_files:
  title = ' '.join(word.capitalize() for word in fn[:-4].split('_'))
  result.append(
    {
      'title': title,
      'filename': fn
    }
  )

print(json.dumps(result, indent=2))
