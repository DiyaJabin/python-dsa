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

<h2>Pattern Card: Opposite Ends Two Pointers</h2>
<ul>
<li><b>Purpose:</b> Find pairs or compare values from both ends of a sorted array.</li>
<li><b>Time Complexity:</b> O(n)</li>
<li><b>Space Complexity:</b> O(1)</li>
<li><b>When to use:</b> Sorted arrays, pair problems, reducing O(n²) to O(n).</li>
<li><b>Examples:</b> Two Sum II, Valid Palindrome, Container With Most Water.</li>
</ul>

<h2>Pattern Card: Reader-Writer</h2>
<ul>
<li><b>Purpose:</b> Filter or modify an array in-place.</li>
<li><b>Reader:</b> Scans every element.</li>
<li><b>Writer:</b> Marks the boundary of the valid portion of the array.</li>
<li><b>Time Complexity:</b> O(n)</li>
<li><b>Space Complexity:</b> O(1)</li>
<li><b>Examples:</b> Remove Duplicates, Move Zeroes, Remove Element.</li>
</ul>
<<h3>Initialization</h3>
<ul>
<li>If the first element is guaranteed to stay, start the reader from index 1.</li>
<li>Otherwise, start both pointers from index 0.</li>
</ul>
<h3>How do I recognize this pattern?</h3>
<ul>
<li>Need to modify an array in-place.</li>
<li>Need to keep or remove certain elements.</li>
<li>Need O(1) extra space.</li>
<li>Each element is processed once.</li>
</ul>

<h2>Pattern Card: Prefix Sum</h2>
<ul>
<li><b>Purpose:</b> Answer multiple range sum queries efficiently.</li>
<li><b>Idea:</b> Store cumulative sums.</li>
<li><b>Construction:</b> O(n)</li>
<li><b>Range Query:</b> O(1)</li>
<li><b>Extra Space:</b> O(n)</li>
<li><b>Examples:</b> Range Sum Query, Pivot Index.</li>
</ul>

<h3>Formula</h3>
<ul>
<li>If left == 0 → prefix[right]</li>
<li>Otherwise → prefix[right] - prefix[left-1]</li>
</ul>