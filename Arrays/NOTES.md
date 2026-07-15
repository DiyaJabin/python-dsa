<h1>Arrays</h1>
<hr>
<ul>
<li>Elements are stored in contiguous memory locations</l1>
<li>Because the elements are stored continuously, the computer can calculate where any element is. That’s why indexing is so fast</li>
<li>Python’s list is a <b>dynamic array</b>, as in it behaves like an array but can grow when needed
</ul>

<h2>Why does indexing start at 0 and how does it take O(1) time?</h2>
<p>Suppose there's an array that starts at the memory location 1000. If the element at position 2 is to be accessed, the computer calculates it  using the formula<br>Address= base address+index*size of element(4 for integer)<br> Hence it immediately knows where the element is, resulting in a time complexity of O(1).</p>
<p>Now if the indedxing were to start from 1 instead of 0, the formula would become:<br>
Address=base address+(index-1)*size of element<br>
Every single array access would require an extra subtraction, hence starting the indexing with 0 makes things easier

<h2>Python Lists</h2>
<p>Python lists are a little different. It doesn't store the direct numerical values; the references to the Python objects are stored. However, for DSA, it's better to consider Python lists as dynamic arrays atleast in the algorithm's point of view.

<h2>Amortized O(1)</h2>
<p>Most append operations are O(1).Occassionaly, python has to create a larger list, copy everything and then add the extra element. That copying takes a time complexity of O(n).It doesn't increase the array size by just 1 every time, instead extra space is allocated to accomodate future appends as well.But since resizing doesn’t happen every time, the average cost over many appends stay close to constant time.So we say that list.append() has an amortized time complexity of O(1).

<h2>Time complexity summaries</h2>
<ul>
<li>Indexing → O(1)</li>
<li>Changing an element → O(1)</li>
<li>Appending → amortized O(1)</li>
<li>Inserting at the front → O(n) (You have to shift every element to the right)</li>
<li>Deleting from the front → O(n) (Every element moves)</li>
<li>Searching → O(n)</li>

