/* 응집도 : 메서드가 변수를 더 많이 사용할수록 메서드와 클래스는 응집도가 더 높다 */

// Stack.java 응집도가 높은 클래스
public class Stack {
    private int topOfStack = 0;
    List<Integer> elements = new LinkedList<Integer>();

    public int size() {
        return topOfStack;
    }

    public void push(int element) {
        topOfStack++;
        elements.add(element);
    }

    public int pop() throws PoppedWhenEmpty {
        if (topOfStack == 0)
            throw new PoppedWhenEmpty();
        int element = element.get(--topOfStack);
        element.remove(topOfStack);
        return element;
    }
}