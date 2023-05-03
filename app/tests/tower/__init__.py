from config.tower import tower_base_url


class UserType:
    normal = "일반"
    kakao = 'kakao'
    naver = 'naver'
    apple = 'apple'

class ProductStatus:
    sale = '판매중'
    wait = '대기'
    stop = '정지'

class Category:
    hiphop = '힙합'
    balad = '발라드'
    dance = '댄스'

class ProductCreateAlert:
    product_create_success = '상품 생성 성공'
    product_create_without_data = '모든데이터를 입력해주세요'
    
class CopyrightCreateAlert:
    copyright_create_alert = '저작권 생성 성공'
    copyright_id_is_duplicated_alert = 'Copyright의 Id은/는 이미 존재합니다.'

class CRMAlert:
    crm_create_success = '게시물 생성 성공'
    crm_update_success = '게시물 수정 성공'
    crm_status_update_success = '게시물 상태 업데이트 성공'

class CRMStatus:
    post = '게시 완료'
    wait = '대기'
    delete = '삭제'


class PremiumStatus:
    sale = '판매중'
    wait = '대기'
    stop = '정지'

class PremiumProductAlert:
    create_success = '상품 생성 성공'
    create_fail = '모든데이터를 입력해주세요'

    



