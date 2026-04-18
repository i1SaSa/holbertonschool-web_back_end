# Python Async Comprehension
This repository contains examples of using asynchronous comprehensions in Python. Asynchronous comprehensions allow you to create lists, sets, or dictionaries using asynchronous iterators, making it easier to work with asynchronous data sources.
## Examples
1. **Asynchronous List Comprehension**:
```python
import asyncio
async def async_generator():
	for i in range(5):
		await asyncio.sleep(1)
		yield i
async def main():
	async for item in async_generator():
		print(item)
asyncio.run(main())
```
2. **Asynchronous Set Comprehension**:
```python
import asyncio
async def async_generator():
	for i in range(5):
		await asyncio.sleep(1)
		yield i
async def main():
	async for item in async_generator():
		print(item)
asyncio.run(main())
```
3. **Asynchronous Dictionary Comprehension**:
```python
import asyncio
async def async_generator():
	for i in range(5):
		await asyncio.sleep(1)
		yield i
async def main():
	async for item in async_generator():
		print(item)
asyncio.run(main())
```
## Conclusion
Asynchronous comprehensions are a powerful feature in Python that allows you to work with asynchronous data sources in a more concise and readable way. By using async generators and async for loops, you can easily create lists, sets, or dictionaries from asynchronous data without blocking the main thread. This can be particularly useful when dealing with I/O-bound tasks, such as fetching data from a web API or reading from a database.
Feel free to explore the examples provided in this repository and experiment with your own asynchronous comprehensions!
