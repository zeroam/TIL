const loggerMiddleware = store => next => action => {
  // 현재 스토어 상태 값 기록
  console.log('현재 상태', store.getState())
  // 액션 기록
  console.log('액션', action)

  // 액션을 다음 미들웨어 또는 리뉴서로 넘김
  const result = next(action)

  // 액션 처리 후의 스토어 상태를 기록함
  console.log('다음 상태', store.getState())
  console.log('\n')

  return result
}

export default loggerMiddleware