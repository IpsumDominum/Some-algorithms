import openai
import io
openai.api_key = "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"

l = openai.File.list()

def get_file_id(file_name):
    for item in l.data:
        if(item.filename==file_name):
            return item.id
    return None
file_id = get_file_id("test_file_hi")
if(file_id!=None):
    class Test:
        def __init__(self,file_name,file):
            self.name = file_name
            self.file = file
        def read(self):
            return self.file
            
    a = Test("test_file_hi","""{"text":"hi"}""")
    f = openai.File.create(
    file=a,
    purpose='answers'
    )
else:
    pass
a = openai.Engine("ada").search(
    search_model="ada", 
    query="hi", 
    max_rerank=5,
    file=file_id
)
print(a)
"""
{
  "bytes": 15,
  "created_at": 1649938391,
  "filename": "file",
  "id": "file-Kfw3206FDsd6bU49NOTyGA3H",
  "object": "file",
  "purpose": "answers",
  "status": "uploaded",
  "status_details": null
}
"""