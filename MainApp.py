# import PIL.Image as pil
# import io
#
# fname = 'C:\\Users\\sai.kurakula\\Downloads\\VID_20190822_065609.mp4'
# fname2 = 'C:\\Users\\sai.kurakula\\Desktop\\VID_20190822_065609_1.mp4'
# with open(fname,'rb+') as file:
#     data = file.read()
#
# # image = pil.open(io.BytesIO(data))
# im = pil.open(fname)
# im.show()
# # im.thumbnail((250,250))
# # imgByteArr = io.BytesIO()
# # im.save(imgByteArr, format='PNG')
# # imgByteArr = imgByteArr.getvalue()
# # with open(fname2,'wb') as f:
# #     f.write(imgByteArr)
# # im.show()



from WordsInOceanOfLetters import WordsInOceanOfLetters

# ImagePath = 'C:\\Users\\sai.kurakula\\Desktop\\words.jpg'
# TesseractPath = 'C:\\Users\\sai.kurakula\\Desktop\\Tesseract\\tesseract.exe'
BASEDIR = 'E:\\PyCharm\\WordsInOceanOfLetters\\Word lists in csv\\'
# fileName = 'Aword.csv'
# pandas_data = pd.read_csv(os.path.join(BASEDIR,fileName),sep='delimiter',header=None)

# has_data = pandas_data[pandas_data[0].str.startswith('aetiology') == True].drop_duplicates()

# print(has_data.__len__())
# print(pandas_data[:0].filter(like='ae',axis=1))

# pytesseract.pytesseract.tesseract_cmd = TesseractPath
data = """
JGLDMGkDMSDOEOYMSCMWOQPRYTLSMLFJOMCES
KOGJKLMSMIEOPJMLSMVMGKEJSKNMLESSONSJAPQ
PEICREATIONJMXLAMFAJFLSMCGJIWLPVEPJFLAMVL
WILFEGMLEMFMEPAVBNZLSNVMJDKUITEWJTKDKNV
MSAGKDSLJGKDLSJGKLSGRATITUDEJGKLSJAKLGZV
NMCNSJWUQDLDPWSJGDSKlEMNBSKGMNBAXBDMSII
IMELNGSANVDCONNECTIONKMGEWJNNZCMANHHFL
NQIRPWIQTYIEJCZXNMXZVJSAGKSMZNVLGKELJWJK
TNSNJDQRWADFXCRPWVGCRBYTNMONEYKUMLIMLY
UJVRNWCGEYVQPOWERPUYXDRWKLJDSKLGJKDSLJI
IALIGNMENTJEVMSLJJFLSHAHMLFJELWPORIVMSMM
TGLDMGKDMSIOMCHANGEVVMSCMWOQPRYTLSMLFJ
IJMCESKOGJKLMSMIEOPJMLSMVMGKEJSKNMJAPQPE
OOMXLAMFAHEALTHJFLSMCGJIWPJFLAMVLWILFEGM
NNMFMEPAVBNZLSNVMJDKUISELFCAREVMSNGKDSL
JGKDLSJGKLSJGKLSJAKLGZVNMCNSJWUQDLDPWSJ
GDSKIEMNBSKGMNBAXBDMSGMELNGSANVDSMGEW
JNNZCMANHHFLSTRENGTHWQIRPWIQTYIEJCZXNMR
ZVJSAGKSMZNVLGKELJWJKCNSNFAMILYJDQRWADE
XCRSWVGCRBYTNKUMLIMLYBJVRNWCGEYVQXDRWS
LJDSKLWPURPOSEJKDSLJEMJGLDMGKDMSDOEOVM
STMWOQMIRACLESPRYTLSMLFJOMCESKOGJKLMSMI
ELPJMLSMVMGKEJSKNMJAPQBREAKTHROUGHPEjJM
XLAMFAJFLSGMDTVNMWURHDKABNPOIUMAFNHAKHJ
JJHJJDHJSWIIRUMAMBQGEHJAKQWHCSANKNLALADI
"""
# print(pytesseract.image_to_string(Image.open(ImagePath)))
# dataArray = data.split('\n')


data = WordsInOceanOfLetters(data,BASEDIR)

print(data.getWordsFromLine())