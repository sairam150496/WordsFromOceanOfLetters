import os
try:
    import pytesseract
except:
    print('Please Wait while We Install pyTesseract')
    try:
        os.system('pip install pyTesseract')
    except Exception as excp:
        print('Please install pip')
try:
    from PIL import Image
except:
    print('Please Wait while We Install Pillow')
    try:
        os.system('pip install pillow')
    except Exception as excp:
        print('Please install pillow')
try:
    import pandas as pd
except:
    print('Please Wait while We Install Pandas')
    try:
        os.system('pip install pandas')
    except Exception as excp:
        print('Please install pandas')
class WordsInOceanOfLetters:
    def __init__(self,tesseractData,wordsDirectory):
        self.imageData = tesseractData
        self.csvPath = wordsDirectory
        self.finalWords = []

    def tesseractStringExtrction(self,tesseractPath,imagePath):
        try:
            pytesseract.pytesseract.tesseract_cmd = tesseractPath
            return pytesseract.image_to_string(Image.open(imagePath))
        except Exception as exception:
            return exception
    def getWordsFromLine(self):
        arrayOfLines = [x for x in self.imageData.split('\n') if len(x)>0]
        totalWords = []
        for i in range(len(arrayOfLines)):
            totalWords.append(self.getArrayOfWordsFromLine(arrayOfLines[i]))
        return set(self.finalWords)
    def getArrayOfWordsFromLine(self,line):
        words = []
        characterSequence = ''
        for eachItem in range(len(line)-1):
            characterSequence += line[eachItem]+line[eachItem+1]
            isTrue = False
            wordFound = self.checkWeatherWordExist(characterSequence)
            if  wordFound == 'partially true':
                try:
                    tempSequence = characterSequence + line[eachItem + 2]
                except:
                    continue
                count = 2
                while True:
                    doesWordExist = self.checkWeatherWordExist(tempSequence)
                    if doesWordExist == 'true':
                        isTrue = True
                        break
                    elif doesWordExist == 'partially true':
                        count+=1
                        try:
                            tempSequence = tempSequence + line[eachItem + count]
                        except:
                            break
                    else:
                        characterSequence = ''
                        break
                if isTrue == True:
                    words.append(line[eachItem:count])
                    characterSequence = ''

            elif wordFound == 'true':
                words.append(characterSequence)
                characterSequence = ''
            else:
                characterSequence = ''

        return words




    def checkWeatherWordExist(self,charSequence):
        # print(charSequence)
        fileName = charSequence[0].upper()+'word.csv'
        wordData = pd.read_csv(self.csvPath+fileName,sep='delimiter',header = None)
        try:
            countOfWords = wordData[wordData[0].str.startswith(charSequence.lower()) == True].drop_duplicates().__len__()
            exactWord = wordData[(wordData[0].str.startswith(charSequence.lower()) == True) & (wordData[0].str.len() == len(charSequence.lower())) == True].drop_duplicates().__len__()
            # print(countOfWords)
            # print(exactWord)
            if(exactWord == 1):
                self.finalWords.append(charSequence)
                if(countOfWords > 1):
                    return 'partially true'
                return 'true'
            elif countOfWords >= 1 and exactWord !=1:
                return 'partially true'
            else:
                return 'false'
        except Exception as e:
            print(e)
            return 'exception'