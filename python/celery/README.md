## Celery

### 참조링크

- [Understand how celery works by building a clone](https://www.komu.engineer/blogs/celery-clone/understand-how-celery-works)



### Intro

- delayed job processor(또는 background process, asynchronous task queue 등으로 불림)는 나중에 코드를 실행할 수 있는 소프트웨어 시스템이다.

- 이러한 소프트웨어의 예로는 [Celery](https://github.com/celery/celery), [Resque](https://github.com/resque/resque), [Sidekiq](https://sidekiq.org/) 등이 있다

- background task processor가 필요한 경우
  - 전자상거래(e-commerce) 웹사이트>
  - 주문 확인 메시지 표시
  - 데이터베이스에 대한 주문 승인
  - 주문 메트릭 이벤트 전송
  - 고객에게 확인 이메일 보내기
  - 등등