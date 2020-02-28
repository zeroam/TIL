// 명령과 조회를 분리하라!
if (set("username", "unclebob"))...

// -->
if (attributeExists("username")) {
    setAttribute("username", "unclebob");
    ...
}