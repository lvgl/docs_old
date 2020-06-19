function add_version_selector()
{
  p = document.getElementById("rtd-search-form").parentElement;
  p.innerHTML = `
<select name="versions" id="versions" onchange="ver_sel()" style="border-radius:5px; margin-bottom:15px">
  <option value="latest">latest</option>
  <option value="dev">development</option>
  <option value="v7">release/v7</option>
  <option value="v6">release/v6</option>
</select>` + p.innerHTML;
}

function ver_sel()
{
  var x = document.getElementById("versions").value;
	window.location.href = "https://docs.lvgl.io/" + x + "/en/html";

}

document.addEventListener('DOMContentLoaded', (event) => {
    add_version_selector();
})
