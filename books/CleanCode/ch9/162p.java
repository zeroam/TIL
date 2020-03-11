/* 실제 환경과 테스트 완경은 요구사항이 판이하게 다름
  -> 실제 코드만큼 효율적인 필요는 없음
*/
// EnvironmentControllerTest.java
@Test
public void turnOnLoTempAlarmAtThreashold() throws Exception {
    hw.setTemp(WAY_TOO_COLD);
    contoller.tic();
    assertTrue(hw.heaterState());
    assertTrue(hw.blowerState());
    assertFalse(hw.coolerState());
    assertFalse(hw.hiTempAlarm());
    assertTrue(hw.loTempAlarm());
}

// EntironmentControllerTest.java (리팩터링)
@Test
public void turnOnLoTempAlarmAtThreshold() throws Exception {
    wayTooCold();
    assertEquals("HBchL", hw.getState());
}