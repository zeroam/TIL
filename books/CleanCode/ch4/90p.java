// GeneratePrimes.java
/**
 * 이 클래스는 사용자가 지정한 최대 값까지 소수를 생성한다. 사용된 알고리즘은
 * 에라스토테네스의 체다.
 * <p>
 * 에라스토테네스: 기원전 276년에 리비아 키레네에서 출생, 기원전 194년에 사망
 * 지구 둘레를 최초로 계산한 사람이자 달력에 윤년을 도입한 사람.
 * 알렉산드리아 도서관장을 역임
 * <p>
 * 알고리즘은 상당히 단순하다. 2에서 시작하는 정수 배열을 대상으로
 * 2의 배수를 모두 제거한다. 다음으로 남은 정수를 찾아 이 정수의 배수를 모두 지운다.
 * 최대 값의 제곱근이 될 때까지 이를 반복한다.
 * 
 * @author Alphonse
 * @version 13 Feb 2002 atp
 */
import java.util.*;

public class GeneratePrimes
{
    /**
     * @param maxValue 는 소수를 찾아낼 최대 값
     */
    public static int[] generatePrimes(int maxValue)
    {
        if (maxValue >= 2)  // 유일하게 유효한 경우
        {
            // 선언
            int s = maxValue + 1;   // 배열 크기
            boolean[] f = new boolean[s];
            int i;

            // 배열을 참으로 초기화
            for (i = 0; i < s; i++)
                f[i] = true;

            // 소수가 아닌 알려진 숫자를 제거
            f[0] = f[1] = false;

            // 체
            int j;
            for (i = 2; i < Math.sqrt(s) + 1; i++) {
                if (f[i]) // i가 남아 있는 숫자라면 이 숫자의 배수를 구한다.
                {
                    for (j = 2 * i; j < s; j += i)
                        f[j] = false;   // 배수는 소수가 아니다.
                }
            }

            // 소수 개수는?
            int count = 0;
            for (i = 0; i < s; i++)
            {
                if (f[i])
                    count++;
            }

            int[] primes = new int[count];

            // 소수를 결과 배열로 이동한다.
            for (i = 0, j = 0; i < s; i++)
            {
                if (f[i])
                    primes[j++] = i;
            }

            return primes;  // 소수를 반환한다.
        }
        else    // maxValue < 2
            return new int[0];  // 입력이 잘못되면 비어 있는 배열을 반환한다.
    }
}