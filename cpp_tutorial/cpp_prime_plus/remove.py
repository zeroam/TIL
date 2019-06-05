import os
import shutil
import re

for folder, subfolders, filenames in os.walk('.'):
    for subfolder in subfolders:
        if subfolder == 'Debug':
            # Debug 폴더는 제거
            shutil.rmtree(os.path.join(folder, subfolder))

    for filename in filenames:
        pattern = '.*\.vcxproj.*'
        result = re.match(pattern, filename)
        if result:
            # .vcxproj 의 이름을 가진 파일 제거
            os.remove(os.path.join(folder, filename))
    