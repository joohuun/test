from datetime import datetime

tower_base_url = "http://10.2.1.100:5001/tower/"
email = 'kimju0612@naver.com'
password = '1234Qwer!!'

query = """
mutation toeknCreate{
    tokenCreate(email: "아이디",
      password: "비밀번호") {
        token
        refreshToken
        csrfToken
        user {
            email
        }
        errors {
            field
            message
        }
    }
}
"""


class AccountData:
    username = '관리자'

class CRMData:
    content_title = '제목 입니다'
    content_body = '내용입니다내용입니다내용입니다내용입니다내용입니다내용입니다내용입니다내용입니다내용입니다'
    news_link = 'https://finance.naver.com/news/news_read.naver?mode=mainnews&office_id=011&article_id=0004160214'
    content_update_title = '수정'
    content_update_body = '수정'
    news_update_link = '수정'


class ProductData:
    product_price = '1000'
    product_amount = '1000'


class CopyrightData:
    copyrigt_id = 'krw'
    copyright_id2 = f'UITEST{datetime.now().second}'
    duple_copyright_id = 'UITEST01'
    copyright_name = '이노래'
    copyrignt_singer = '김가수'
    copyright_yield_rate1 = '200'
    copyright_yield_rate2 = '250'
    youtube_url = 'www.youtube.com'
    yotube_description = 'uitest'
    composer = '김작곡'
    lyricist = '이작사'
    arranger = '김편곡'


class PremiumProductData:
    premium_product_price = '100000'
    premium_product_amount = '1000'


class PremiumCopyrightData:
    copyright_id = '210629N3'
    

