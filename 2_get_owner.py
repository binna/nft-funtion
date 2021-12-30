import pymysql
import requests

host = "DB url"
port = "3306"
database = "db database name"
username = "db username"
password = "db password"


def nft(contact, token):
    my_headers = {"Content-Type": "application/json", "x-chain-id": "8217"}
    response = requests.get(
        "https://th-api.klaytnapi.com/v2/contract/nft/" + contact + "/token/" + token,
        auth=('AccessKey ID', 'Secret AccessKey'),
        headers=my_headers
    )
    return response.json()['owner']


def main():
    conn = pymysql.connect(
        host=host,
        user=username,
        passwd=password,
        db=database,
        charset='utf8'
    )
    cursor = conn.cursor()

    klips = "select * from klip"
    cursor.execute(klips)

    for row in cursor.fetchall():
        owner = nft(row[1], row[2])
        query = "update klip set owner='" + owner + "' where id=" + str(row[0])
        print(query)
        cursor.execute(query)
        conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
    print("프로그램 종료")
