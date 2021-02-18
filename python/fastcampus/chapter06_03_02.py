"""파이썬 심화
Future 동시성
비동기 작업 실행
- 지연시간(Block) CPU 및 리소스 낭비 방지 -> Network I/O 관련 작업 동시성 활용 권장
- 적합한 작업일 경우 순차 진행보다 압도적으로 성능 향상
"""
import os
import time
import sys
import csv
from concurrent import futures

# concurrent.futures 방법1(ThreadPoolExecutor, ProcessPoolExecutor)
# map()
# 서로 다른 스레드 또는 프로세스에서 실행 가능
# 내부 과정 알 필요 없으며, 고수준으로 인터페이스 제공

# Google Python GIL(Global Interpreter Lock)
# 한번에 하나의 스레드만 실행
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
def separate_many(nt):
    # 분리 데이터
    data = get_sales_data(nt)

    # 상황 출력
    show(nt)

    # 파일 저장
    save_csv(data, f"{nt.lower()}.csv")

    return nt


def main(separate_many):
    # worker 개수
    worker = min(20, len(NATION_LS))

    start_tm = time.time()
    # ThreadPoolExecutor : GIL 종속
    with futures.ThreadPoolExecutor(worker) as executor:
    # ProcessPoolExecutor : GIL 우회, 변경 후 -> os.cpu_count()
    # with futures.ProcessPoolExecutor(worker) as executor:
        # map -> 작업 순서 유지, 즉시 실행
        result = executor.map(separate_many, sorted(NATION_LS))
    end_tm = time.time() - start_tm

    print(f"\n{list(result)}, csv separated in {end_tm:.2f}")


if __name__ == "__main__":
    main(separate_many)
