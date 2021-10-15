from time import sleep


def get_number_query(column):
    query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^[-]?\d+(\.?\d*)$');".format(
        column, filename, '"index"', column)
    # queries.append(query)
    return query


def get_date_query(column, form):
    # 일단 시간 생략
    if form == "YYYY-MM-DD":
        query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^(19|20)\d{}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[0-1])$');".format(
            column, filename, '"index"', column, 2)
        # queries.append(query)
    elif form == "YYYY":
        query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^(19|20)\d{}$');".format(
            column, filename, '"index"', column, 2)
        # queries.append(query)
    elif form == "MM":
        query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^(0[1-9]|1[012])$');".format(
            column, filename, '"index"', column)
    elif form == "DD":
        query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^(0[1-9]|[12][0-9]|3[0-1])$');".format(
            column, filename, '"index"', column)
    elif form == "YYYY-MM":
        query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^(19|20)\d{}-(0[1-9]|1[012])$');".format(
            column, filename, '"index"', column, 2)
    elif form == "MM-DD":
        query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[0-1])$');".format(
            column, filename, '"index"', column)
    return query


def get_price_query(column):
    query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^[-]?\d+(\.?\d*)$');".format(
        column, filename, '"index"', column)
    # queries.append(query)
    return query


def get_percent_query(column):
    query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^[-]?\d+(\.?\d*)$');".format(
        column, filename, '"index"', column)
    # queries.append(query)
    return query


def get_phone_number_query(column):
    query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^[0-9]{}-[0-9]{}-[0-9]{}$');".format(
        column, filename, '"index"', column, "2,3", "3,4", 4)
    # queries.append(query)
    return query


def get_business_number_query(column):
    query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^[0-9]{}-[0-9]{}-[0-9]{}$');".format(
        column, filename, '"index"', column, 3, 2, 5)
    # queries.append(query)
    return query


def get_email_query(column):
    query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$');".format(
        column, filename, '"index"', column)
    # queries.append(query)
    return query


def get_whether_query(column):
    query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND UPPER({}) not in ('Y', 'N‘ , ‘1’ ,’0’ );".format(
        column, filename, '"index"', column)
    # queries.append(query)
    return query


def get_zip_code_query(column):
    query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^[0-9]{}$');".format(
        column, filename, '"index"', column, 5)
    return query


def query_generator():
    global filename
    global queries
    queries = []
    # 파일 이름: 한번만 입력
    print("파일 이름을 입력하세요...")
    try:
        filename = input()
    # 잘못 입력한 경우
    except:
        print("잘못 입력")
    try:
        while True:
            #컬럼, 데이터타입
            print("컬럼과 데이터 타입을 입력하세요.")
            try:
                column, data_type = input().split()
                if data_type == "숫자":
                    query = get_number_query(column)
                elif data_type == "날짜":
                    print("형식을 입력해주세요.")
                    form = input()
                    query = get_date_query(column, form)
                elif data_type == "금액":
                    query = get_price_query(column)
                elif data_type == "율":
                    query = get_percent_query(column)
                elif data_type == "전화번호" or data_type == "전화 번호":
                    query = get_phone_number_query(column)
                elif data_type == "사업자번호":
                    query = get_business_number_query(column)
                elif data_type == "이메일":
                    query = get_email_query(column)
                elif data_type == "여부":
                    query = get_whether_query(column)
                elif data_type == "우편번호":
                    query = get_zip_code_query(column)
                else:
                    print("지정된 데이터 타입이 아닙니다.")
            # 잘못 입력한 경우
            except TypeError:
                print("데이터 타입을 입력하지 않았습니다.")
            except ValueError:
                print("컬럼을 입력하지 않았습니다.")
            queries.append(query)
    except KeyboardInterrupt:
        print("==========================================")
        print("프로그램을 종료합니다.")
    return queries, filename


def make_txt(filename):
    txt_filename = '{} SQL 쿼리.txt'.format(filename)
    f = open(txt_filename, 'w')
    for query in queries:
        f.write(query+"\n")
    f.close()


if __name__ == "__main__":
    print("쿼리 생성기를 실행합니다.")
    sleep(0.5)
    # 이부분 좀 고쳐야될거같은데
    print("입력을 마치려면 ctrl+c를 눌러주세요.")
    print("=========================================")
    sleep(1)
    query_generator()
    make_txt(filename)
