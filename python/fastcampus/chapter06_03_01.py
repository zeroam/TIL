"""파이썬 심화
Future 동시성
비동기 작업 실행
- 적합한 작업일 경우 순차 진행보다 압도적으로 성능 향상
"""
import os
import time
import sys
import csv

# 순차 실행 예제
NATION_LS = "Singapore Germany Israel Norway Italy Canada France Spain Mexico".split()
TARGET_CSV = "./resources/nations.csv"
DEST_DIR = "./csvs"
HEADER = [
    "Region",
    "Country",
    "Item Type",
    "Sales Channel",
    "Order Priority",
    "Order Date",
    "Order ID",
    "Ship Date",
    "Units Sold",
    "Unit Price",
    "Unit Cost",
    "Total Revenue",
    "Total Cost",
    "Total Profit",
]


def save_csv(data, filename):
    path = os.path.join(DEST_DIR, filename)

    with open(path, "w", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=HEADER)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def get_sales_data(nt):
    with open(TARGET_CSV, "r") as f:
        reader = csv.DictReader(f)
        data = []
        # print(reader.fieldnames)  # Header 확인
        for r in reader:
            if r["Country"] == nt:
                data.append(r)

    return data


def show(nt):
    print(nt, end=" ")
    sys.stdout.flush()


# 국가별 분리 함수 실행
def separate_many(nt_list):
    for nt in sorted(nt_list):
        # 분리 데이터
        data = get_sales_data(nt)

        # 상황 출력
        show(nt)

        # 파일 저장
        save_csv(data, f"{nt.lower()}.csv")
    return len(nt_list)


def main(separate_many):
    start_tm = time.time()
    result_cnt = separate_many(NATION_LS)
    end_tm = time.time() - start_tm

    print(f"\n{result_cnt}, csv separated in {end_tm:.2f}")


if __name__ == "__main__":
    main(separate_many)
