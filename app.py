import pikepdf

def getAttachments(pdf):
      catalog = pdf.trailer["/Root"]
      fileNames = catalog['/Names']['/EmbeddedFiles']['/Names']
      attachments = {}
      for index in range(1, len(fileNames), 2):
        name = str(fileNames[index]['/UF'])
        fData = fileNames[index]['/EF']['/F']
        attachments[name] = fData.read_bytes()

      return attachments

pdf = pikepdf.open('input_files/files-attached.pdf')
dictionary = getAttachments(pdf)
for key,value in dictionary.items():
    with open(f'exported/{key}', 'wb') as output:
        output.write(value)
print('data exported')