from bs4 import BeautifulSoup
import requests

'''
 tensorflow API information
 - Document Address
 - GitHub Source Address
 - API Arguments
 - API Example code
 
 example:
 tf = tf()
 tf.get_info('tf.keras.layers.Conv2D')

 주의
 - tf.keras.- api , tf.applications.- api는 대부분 가능함
 - get_info에 String type으로 전달해야함

'''
class tf:

    def __init__(self):
        pass

    # get GitHub address
    def get_gitHub(self, soup):

        git = soup.find('table',{'class':'tfo-api'})
        if git is None:
            print("libaray is not available.")
            print("Right example: keras.callbacks.EarlyStopping")
            return False
        else:
            print("* Git Hub source *")
            result = git.find('a',{'target':'_blank'})['href']
            print(f"[GitHub]({result})")
    
    # get API arguments
    def get_args(self,soup):

        arg = soup.find('pre',{'class':'lang-py'})
        if arg is None:
            print("libaray is not available.")
            print("Right example: keras.layers.Cov2D")
        else:
          argument = arg.text.lstrip()
          print("* Arguments *")
          print(argument)

    # get Example code
    def get_ex(self,soup) -> None:

        print("* Code Examples *")
        code_tags = soup.find_all('code', {'class': 'devsite-terminal'})
        if code_tags is None:
            print("libaray is not available.")
            print("Right example: keras.optimizers.Adam")
        else:
            for code_tag in code_tags:
                code_text = code_tag.get_text(strip=True)
                print(">>> ",code_text)

    # get total information
    def get_info(self,input:str):
        assert type(input) == str , f"{input} must be a String type"
        # tensorflow API
        input = input.split('.')

        # tensorflow Document url
        for index,i in enumerate(input):
            if index == 0 and i == 'tf':
                url = f'https://www.tensorflow.org/api_docs/python/'
            elif index == 0 and i == 'keras':
                url = f'https://www.tensorflow.org/api_docs/python/tf/'
            url += i + '/'
        html = requests.get(url).text 
        soup = BeautifulSoup(html, 'html.parser')

        # print tensforflow API Info
        print("===============================================")
        print('* Document *')
        print(url)
        print(' ')
        self.get_gitHub(soup)
        print(' ')
        self.get_args(soup)
        self.get_ex(soup)
        print("===============================================")

# example usage
# x = tf()
# print(x.get_info('tf.keras.layers.Dropout'))
# print(x.get_info('keras.layers.Dropout'))
