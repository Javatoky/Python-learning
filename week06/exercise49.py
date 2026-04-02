import asyncio


async def process_document(doc_name: str, processing_time: float):
    print(f"[开始] {doc_name}")
    await asyncio.sleep(processing_time)
    print(f"[完成] {doc_name}")
    return {
        "doc": doc_name,
        "time": processing_time,
        "status": "done"
    }

async def batch_process(documents: list[tuple[str, float]]) -> list[dict]:
    return list(
        await asyncio.gather(
            *(process_document(*doc) for doc in documents)
        )
    )

async def batch_process_with_limit(documents: list[tuple[str, float]], max_concurrent: int) -> list[dict]:
    # 限制最大并发数
    sem = asyncio.Semaphore(max_concurrent)

    # Semaphore限流的标准写法：函数封装：每个协程执行前获取许可，返回执行结果，这样就调用这个函数会默认加限流，剩下的逻辑和之前一样
    async def process_with_limit(document: tuple[str, float]):
        async with sem:     # 获取一个许可，没有就暂停等待
            return await process_document(*document)
    
    return list(
        await asyncio.gather(
            *(process_with_limit(doc) for doc in documents)     # asyncio.gather接受多个协程对象，他不能调用生成器得到多个协程对象，所以必须对生成器对象解包：*()
        )
    )