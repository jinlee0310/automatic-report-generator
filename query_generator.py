from time import sleep
import re


def get_number_query(column):
    query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^[-]?\d+(\.?\d*)$');".format(
        column, filename, '"index"', column)
    # queries.append(query)
    return query


def get_date_query(column, form):
    if form == "YYYY" or form == "년도" or form == "연도":
        query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^(19|20)\d{}$');".format(
            column, filename, '"index"', column, 2)

    elif form == "YYYY-MM" or form == "년월":
        query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^(19|20)\d{}-(0[1-9]|1[012])$');".format(
            column, filename, '"index"', column, 2)

    elif form == "YYYY-MM-DD" or form == "년월일":
        query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^(19|20)\d{}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[0-1])$');".format(
            column, filename, '"index"', column, 2)

    elif form == "YYYY-MM-DD HH24" or form == "년월일 시" or form == "년월일시":
        query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^(19|20)\d{}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[0-1])])\s([1-9]|[01][0-9]|2[0-4])$');".format(
            column, filename, '"index"', column, 2)

    elif form == "YYYY-MM-DD HH24:MI" or form == "년월일 시분" or form == "년월일시분":
        query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^(19|20)\d{}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[0-1])])])\s([1-9]|[01][0-9]|2[0-4])[:]([0-5][0-9])$');".format(
            column, filename, '"index"', column, 2)

    elif form == "YYYY-MM-DD HH24:MI:SS" or form == "년월일 시분초" or form == "년월일시분초":
        query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^(19|20)\d{}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[0-1])])])\s([1-9]|[01][0-9]|2[0-4])[:]([0-5][0-9])[:]([0-5][0-9])$');".format(
            column, filename, '"index"', column, 2)

    elif form == "MM" or form == "월":
        query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^(0[1-9]|1[012])$');".format(
            column, filename, '"index"', column)

    elif form == "MM-DD" or form == "월일":
        query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[0-1])$');".format(
            column, filename, '"index"', column)

    elif form == "MM-DD HH24:MI" or form == "월일 시분" or form == "월일시분":
        query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[0-1])\s([1-9]|[01][0-9]|2[0-4])[:]([0-5][0-9])$');".format(
            column, filename, '"index"', column)

    elif form == "DD" or form == "일":
        query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^(0[1-9]|[12][0-9]|3[0-1])$');".format(
            column, filename, '"index"', column)

    elif form == "HH24" or form == "시":
        query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^([1-9]|[01][0-9]|2[0-4])$');".format(
            column, filename, '"index"', column)
    elif form == "HH24:MI" or form == "시분":
        query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^([1-9]|[01][0-9]|2[0-4])[:]([0-5][0-9])$');".format(
            column, filename, '"index"', column)
    elif form == "HH24:MI:SS" or form == "시분초":
        query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^([1-9]|[01][0-9]|2[0-4])[:]([0-5][0-9])[:]([0-5][0-9])$');".format(
            column, filename, '"index"', column)
    elif form == "MI" or form == "분":
        query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^([0-5][0-9])$');".format(
            column, filename, '"index"', column)
    elif form == "MI:SS" or form == "분초":
        query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^([0-5][0-9])[:]([0-5][0-9])$');".format(
            column, filename, '"index"', column)
    elif form == "SS" or form == "초":
        query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'^([0-5][0-9])$');".format(
            column, filename, '"index"', column)
    else:
        print("형식이 올바르지 않습니다.")
    try:
        return query
    except UnboundLocalError:
        pass


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


def get_alpha_query(column):
    query = "SELECT {} FROM C##OPENDATA.{} WHERE {}<>0 AND NOT REGEXP_LIKE({},'[[:alpha:]]');".format(
        column, filename, '"index"', column)
    return query


def get_filename():
    global filename
    global queries
    queries = {}
    print("입력을 마치려면 ctrl+c를 눌러주세요.")
    print("=========================================")
    sleep(1)
    # 파일 이름: 한번만 입력
    print("파일 이름을 입력하세요...")
    try:
        filename = input()
    except KeyboardInterrupt:
        print("==========================================")
        print("프로그램을 종료합니다.")
    # 잘못 입력한 경우
    except:
        print("파일 형식이 잘못되었습니다.")
    return filename


def query_generator():
    try:
        while True:
            #컬럼, 데이터타입
            print("컬럼과 데이터 타입을 입력하세요...")
            try:
                reg = re.compile('^(c|C)[0-9]+$')
                column, data_type = input().split()
                if reg.match(column):
                    if data_type == "숫자":
                        query = get_number_query(column)
                    elif data_type == "날짜":
                        print("형식을 입력해주세요...")
                        form = input()
                        query = get_date_query(column, form)
                    elif data_type == "금액":
                        query = get_price_query(column)
                    elif data_type == "율":
                        query = get_percent_query(column)
                    elif data_type == "전화번호" or data_type == "전화 번호":
                        query = get_phone_number_query(column)
                    elif data_type == "사업자번호" or data_type == "사업자 번호":
                        query = get_business_number_query(column)
                    elif data_type == "이메일":
                        query = get_email_query(column)
                    elif data_type == "여부":
                        query = get_whether_query(column)
                    elif data_type == "우편번호" or data_type == "우편 번호":
                        query = get_zip_code_query(column)
                    elif data_type == "영문명":
                        query = get_alpha_query(column)
                    else:
                        print("지정된 데이터 타입이 아닙니다.")
                        continue
                    try:
                        if column in queries.keys():
                            print("중복 입력 하였습니다.")
                        else:
                            if query is not None:
                                queries[column] = query
                    except UnboundLocalError:
                        pass
                else:
                    print("컬럼 형식이 잘못되었습니다.")
            # 잘못 입력한 경우
            except TypeError:
                print("데이터 타입을 입력하지 않았습니다.")
            except ValueError:
                print("컬럼 또는 데이터 타입을 입력하지 않았습니다.")

    except KeyboardInterrupt:
        print("==========================================")
        print("입력을 종료합니다.")
    return queries


def make_txt(filename):
    txt_filename = '{} SQL 쿼리.txt'.format(filename)
    f = open(txt_filename, 'w')
    for query in queries.values():
        if query is not None:
            f.write(query+"\n")
    f.close()
    sleep(0.5)
    print("쿼리가 저장되었습니다.")


if __name__ == "__main__":
    print("쿼리 생성기를 실행합니다...")
    sleep(0.5)
    get_filename()
    query_generator()
    make_txt(filename)
