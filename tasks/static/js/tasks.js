var lists = [];
function appendTask() {
	var task = document.getElementById('task').value;
	var list = document.getElementById('list').value;
	var date = document.getElementById('date').value;
	var text = ' ' + task + ', in: ' + list + ' Due: ' + date;
	$(".todo").append('<div class="task" id="adding" onclick="done()"></div>');
	var para = document.createElement('p');
	var task = document.createTextNode(text);
	para.appendChild(task, list);
	document.getElementById('adding').appendChild(para);
	$('#adding').removeAttr('id');
	var first = document.getElementById('NoTask');
	first.remove(first.selectedIndex);
} 

function appendList() {
	var list = document.getElementById('newList').value;
	var len = lists.length;
	var n = len++;
	lists[n] = list;
	var text = "";
	for (i = 0; i < len; i++) {
		text += '<option value="'+ lists[i] + '">' + lists[i] + '</option>';
	}
	document.getElementById("list").innerHTML = text;
}

function newTask() {
    $('.addTask').toggle();
	$('.addList').hide();	
}

function newList() {
	$('.addList').toggle();
	$('.addTask').hide();
}

function done() {
    $(event.currentTarget).toggleClass('done');
	$(event.currentTarget).toggleClass('task');	
	$('.done').appendTo('.finished');
	$('.task').appendTo('.todo');
	var none = document.getElementById('NoFinTask');
	none.remove(none.selectedIndex);
}