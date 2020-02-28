// 오류 코드보다 예외를 사용하라
if (deletePage(page) == E_OK) {
    if (registry.deleteReference(page.name) == E_OK) {
        if (configKeys.deleteKey(page.name.makeKey()) == E_OK) {
            logger.log("page deleted");
        } else {
            logger.log("configKey not deleted");
        }
    } else {
        logger.log("delete failed");
        return E_ERROR;
    }
}

// --> 오류 코드 대신 예외를 사용
try {
    deletePage(page);
    registry.deleteReference(page.name);
    configKeys.deleteKey(page.name.makeKey());
}
catch (Exception e) {
    logger.log(e.getMessage());
}

// --> try/catch 블록을 별도 함수로 뽑아냄
public void delete(Page page) {
    try {
        deletePageAndReferences(page);
    }
    catch (Exception e) {
        logError(e);
    }
}

private void deletePageAndReferences(Page page) throws Excpetion {
    deletePage(page);
    registry.deleteReference(page.name);
    configKeys.deleteKey(page.name.makeKey());
}

private void logError(Exception e) {
    logger.log(e.getMessage());
}
