from youtube_transcript_api import YouTubeTranscriptApi
from pykospacing import Spacing

# Writing to an excel
# sheet using Python
import xlwt
from xlwt import Workbook

# Workbook is created
wb = Workbook()

sheet1 = wb.add_sheet('Sheet 1')

# Youtube Video id ?v=
video_id = 'jmRt7PBI_Aw'

transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['ko'])
text = ""
# iterate over all available transcripts
for transcript in transcript_list:
    text += transcript['text']

# for the correct spacing
spacing = Spacing()
text_wo_space = text.replace(" ", "")
text = spacing(text_wo_space)

print(text)
sheet1.write(1, 0, text)
wb.save('xlwt example.xls')
