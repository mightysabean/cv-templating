<h1 id="tutorial">Tutorial</h1>
<p>The use of <code>cv-templating</code> is very easy. But you must know what <code>yaml</code> and <code>jinja2</code> are, and how to use it. It is not necessary to be an expert, but a minimum of knowledge is required.</p>
<p>The full specification of <code>yaml</code> are at <a href="http://www.yaml.org/spec/1.2/spec.html">yaml specs</a> (see <em>Chapter 2</em> for a quick intro) or see <a href="http://docs.ansible.com/ansible/YAMLSyntax.html">yaml basics</a>.</p>
<p>For <code>jinja2</code> you should consult <a href="http://jinja.pocoo.org/docs/2.9/">jinja documentation</a>.</p>
<p>For the objective of making a document using a template and a data file, you do not need all the <code>cv-templating</code> project. You just need writing a little script in <code>Python</code> like this (this example is for generating an HTML file), <code>script.py</code>:</p>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"><span class="im">import</span> yaml
<span class="im">import</span> jinja2

data_file <span class="op">=</span> <span class="st">&#39;your/data_file.yaml&#39;</span>
template_directory <span class="op">=</span> <span class="st">&#39;base/template_directory&#39;</span>
<span class="co">&quot;&quot;&quot; where template files refer as the root to be used internally in</span>
<span class="co">templates, not in the python script&quot;&quot;&quot;</span>
template_file <span class="op">=</span> <span class="st">&#39;base/template_directory/template_file.html&#39;</span>
data <span class="op">=</span> yaml.load(<span class="bu">open</span>(data_file, <span class="st">&#39;r&#39;</span>))
output_file <span class="op">=</span> <span class="st">&#39;your/output_file.html&#39;</span>

env <span class="op">=</span> jinja2.Environment(loader<span class="op">=</span>jinja2.FileSystemLoader(templateBaseDir),
                         lstrip_blocks<span class="op">=</span><span class="va">True</span>, 
                         trim_blocks<span class="op">=</span><span class="va">True</span>)
template <span class="op">=</span> env.get_template(template_file)
stream_produced <span class="op">=</span> template.render(data)
<span class="cf">with</span> <span class="bu">open</span>(output_file, <span class="st">&#39;w&#39;</span>) <span class="im">as</span> o:
            o.write(stream_produced)</code></pre></div>
<p>With a data file like this (in the python code <code>your/data_file.yaml</code>):</p>
<div class="sourceCode"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span class="fu">title:</span> My CV
<span class="fu">emails:</span>
  <span class="kw">-</span> yo@aqui.com
  <span class="kw">-</span> me@here.com</code></pre></div>
<p>Using this template (in the python code <code>base/template_directory/template_file.html</code>):</p>
<pre class="django"><code>&lt;!doctype html&gt;
&lt;html&gt;
    &lt;head&gt;
      &lt;meta charset=&quot;utf-8&quot;/&gt;
      &lt;title&gt;{{ title }}&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
      &lt;h1&gt;{{ title }}&lt;/h1&gt;
      &lt;ul&gt;
        {% for email in emails %}
          &lt;li&gt;{{ email }}&lt;/li&gt;
        {% endfor %}
      &lt;/ul&gt;
    &lt;/body&gt;
&lt;/html&gt;</code></pre>
<p>Executing the python <code>script.py</code></p>
<div class="sourceCode"><pre class="sourceCode sh"><code class="sourceCode bash"><span class="kw">python</span> script.py</code></pre></div>
<p>You will obtain the file <code>your/output_file.html</code>:</p>
<div class="sourceCode"><pre class="sourceCode html"><code class="sourceCode html"><span class="er">&lt;</span>!doctype html&gt;
<span class="kw">&lt;html&gt;</span>
    <span class="kw">&lt;head&gt;</span>
      <span class="kw">&lt;meta</span><span class="ot"> charset=</span><span class="st">&quot;utf-8&quot;</span><span class="kw">/&gt;</span>
      <span class="kw">&lt;title&gt;</span>My CV<span class="kw">&lt;/title&gt;</span>
    <span class="kw">&lt;/head&gt;</span>
    <span class="kw">&lt;body&gt;</span>
      <span class="kw">&lt;h1&gt;</span>My CV<span class="kw">&lt;/h1&gt;</span>
      <span class="kw">&lt;ul&gt;</span>
          <span class="kw">&lt;li&gt;</span>yo@aqui.com<span class="kw">&lt;/li&gt;</span>
          <span class="kw">&lt;li&gt;</span>me@here.com<span class="kw">&lt;/li&gt;</span>
      <span class="kw">&lt;/ul&gt;</span>
    <span class="kw">&lt;/body&gt;</span>
<span class="kw">&lt;/html&gt;</span></code></pre></div>
<p>To do the same with LaTeX, you need to change the syntax tokens of jinja. See this <a href="http://flask.pocoo.org/snippets/55/">explanation</a> that is used in <code>cv-templating</code> (se file jinjatex.py).</p>
<p>The <strong>cv-templating</strong> project takes care of the type of render and checks a lot of things necessary for me. You can modify it to reach your goals.</p>
<h2 id="install-cv-templating">Install cv-templating</h2>
<p>Download the <a href="https://github.com/victe/cv-templating/releases">dist file</a> and do:</p>
<div class="sourceCode"><pre class="sourceCode sh"><code class="sourceCode bash"><span class="kw">pip</span> install  cv-templating-x.y.z.tar.gz</code></pre></div>
<p>Where x.y.z should be the numbers of the downloaded version. It is better if you use <a href="https://virtualenv.pypa.io/en/stable/">virtual environment</a>.</p>
<p>For knowing where the program is installed, run this:</p>
<div class="sourceCode"><pre class="sourceCode sh"><code class="sourceCode bash"><span class="kw">python</span> -c <span class="st">&quot;from distutils.sysconfig import get_python_lib; print(get_python_lib())&quot;</span></code></pre></div>
<p>And go to the directory <code>mcv</code> inside the result of the last command. Here is a directory named <code>examples</code> that you should review following the tutorial.</p>
<p>To execute the program:</p>
<div class="sourceCode"><pre class="sourceCode sh"><code class="sourceCode bash"><span class="kw">mcv</span> path/to/config/file.yaml</code></pre></div>
<p>Where <code>path/to/config/file.yaml</code> is the name and path of a config file in <code>YAML</code> format (see below).</p>
<h2 id="check-the-examples">Check the examples</h2>
<p>To examine the examples, go to the directory of the program, then you must do, for HTML:</p>
<div class="sourceCode"><pre class="sourceCode sh"><code class="sourceCode bash"><span class="kw">mcv</span> examples/eucv_en_html.yaml</code></pre></div>
<p>You can see the <a href="Someone.html">HTML document generated</a>.</p>
<p>And for LaTeX:</p>
<div class="sourceCode"><pre class="sourceCode sh"><code class="sourceCode bash"><span class="kw">mcv</span> examples/eucv_en_latex.yaml</code></pre></div>
<p>You can see the <a href="Someone.pdf">PDF document generated</a>.</p>
<h2 id="config-file">Config file</h2>
<p>The config file is the <code>yaml</code> file you pass as a parameter to the <code>mcv.py</code> program. The names of the config files can be anything. Although, it is better if it is something that helps you to easy remember their content. It could be your name, date and place or company you are applying.</p>
<p>Each config file has three main sections: <strong>config</strong>, <strong>doc</strong>, and <strong>data</strong>.</p>
<h3 id="config-section-of-the-config-file">Config section of the config file</h3>
<p>This is the content of the <strong>config</strong> section of the <code>eu_en_html.yaml</code> file in the examples directory (in all <code>yaml</code> files avoid the use of <em>TABs</em>):</p>
<div class="sourceCode"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span class="fu">config:</span>
  <span class="fu">base_dir:</span> <span class="st">&#39;/home/vicente/projects/pro/cv-templating/mcv/examples&#39;</span>
  <span class="fu">output_dir:</span> <span class="st">&#39;output/html&#39;</span>
  <span class="fu">template_base_dir:</span> <span class="st">&#39;html&#39;</span>
  <span class="fu">template_file:</span> <span class="st">&#39;flat_en.html&#39;</span>
  <span class="fu">template_type:</span> html
  <span class="fu">output_filename:</span> <span class="st">&quot;Someone&quot;</span>
  <span class="fu">resources:</span>
    <span class="fu">build:</span>
      <span class="kw">-</span> <span class="kw">[</span><span class="st">&quot;data/figures/bobo.png&quot;</span><span class="kw">,</span> <span class="st">&quot;images/bobo.png&quot;</span><span class="kw">]</span>
      <span class="kw">-</span> <span class="kw">[</span><span class="st">&quot;html/flat_en_resources&quot;</span><span class="kw">,</span> <span class="st">&quot;&quot;</span><span class="kw">]</span>
    <span class="fu">output:</span>
      <span class="kw">-</span> <span class="kw">[</span><span class="st">&quot;data/figures/bobo.png&quot;</span><span class="kw">,</span> <span class="st">&quot;images/bobo.png&quot;</span><span class="kw">]</span>
      <span class="kw">-</span> <span class="kw">[</span><span class="st">&quot;html/flat_en_resources&quot;</span><span class="kw">,</span> <span class="st">&quot;css&quot;</span><span class="kw">]</span></code></pre></div>
<p>You must put in this first section, <strong>config</strong>, information related to the generation, from where the program can find anything else.</p>
<ul>
<li><em>base_dir</em>: you must change this to the directory where you have your data and templates structure,</li>
<li><em>output_dir</em>: where you want the output,</li>
<li><em>template_base_dir</em>: which is the template base directory,</li>
<li><em>template_file</em>: which template want to use,</li>
<li><em>template_type</em>: what kind of template is it (html or latex),</li>
<li><em>output_filename</em>: the prefix of the output file name, date and time will be appended.</li>
<li><em>resources</em>: files and directories to be copied, in the <em>build</em> phase from the source indicated to dest inside a tmp directory. After build, in the <em>output</em> phase, files are copied from src to <em>output_dir</em>.</li>
</ul>
<p>You can not change the name of these variables in the section <strong>config</strong>. You can not also change the name of the three sections (config, doc and data). The content and name of the variables inside the other two section (doc and data) are up to you. You can see how easy is to map variables in data files with the variables in the template files in the examples, and in this tutorial.</p>
<p>The program appends the date to the content of the <em>output_filename</em> variable when the output is generated. <em>base_dir</em> refers to the directory from where the rest of the information in the config file is reachable, <em>template_base_dir</em> relates to the directory from which <em>Jinja</em> can infer the position of other templates when <em>extends</em> (if you use heritance in your templates) will be employed.</p>
<h3 id="doc-section">doc section</h3>
<p>The <strong>doc</strong> section is intended to be used for information related to the configuration of the document itself. For instance, to specify the paper size, orientation, title, keywords, etc. that you could easily change from one type of CV to other (just copy your config.yaml file and change the values).</p>
<p>This is the <strong>doc</strong> section content of the same config file used before:</p>
<div class="sourceCode"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span class="fu">doc:</span>
  <span class="fu">language:</span> <span class="st">&quot;en&quot;</span>
  <span class="fu">title:</span> <span class="st">&quot;Curriculum vitae&quot;</span>
  <span class="fu">bigitem:</span>
    <span class="kw">-</span> <span class="st">&quot;Personal statement&quot;</span>
    <span class="kw">-</span> <span class="st">&quot;Something good about Bobo.&quot;</span></code></pre></div>
<p>And this is where you use the variable in the template file (from the config section, the file must be <code>flat_en.html</code> inside the template base dir <code>html</code> inside of the base structure in <code>/home/vicente/projects/pro/cv-templating/mcv/examples</code>):</p>
<pre class="django"><code>&lt;!DOCTYPE html&gt;
&lt;!-- Based on http://themes.jsonresume.org/theme/flat --&gt;
&lt;html lang={{ language }}&gt;&lt;head&gt;&lt;meta http-equiv=&quot;Content-Type&quot; content=&quot;text/html; charset=UTF-8&quot;&gt;

&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, user-scalable=no, minimal-ui&quot;&gt;
&lt;title&gt;{{ title }}&lt;/title&gt;
...</code></pre>
<p>You just need to put the name of the variable between a pair of curly brackets. In the output file, the content of the variable will be substituted.</p>
<h3 id="data-section">data section</h3>
<p>The <strong>data</strong> section must point to the files that have the stored data. You can use <code>yaml</code> files for unstructured or semi-structured data or <code>csv</code> files for tabular. From the same config file used before:</p>
<div class="sourceCode"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span class="fu">data:</span> <span class="co"># list of data files with a variable name to refer them in the template file.</span>
  <span class="fu">persinfo:</span> <span class="st">&quot;data/pers_info-en.yaml&quot;</span>
  <span class="fu">profinfo:</span> <span class="st">&quot;data/prof_info-en.yaml&quot;</span>
  <span class="fu">acadinfo:</span> <span class="st">&quot;data/acad_info-en.yaml&quot;</span>
  <span class="fu">persskills:</span> <span class="st">&quot;data/pers_skills-en.yaml&quot;</span>
  <span class="fu">additinfo:</span> <span class="st">&quot;data/addit_info-en.yaml&quot;</span>
  <span class="fu">references:</span> <span class="st">&quot;data/references.yaml&quot;</span>
  <span class="fu">curses:</span> <span class="st">&quot;data/acad_info_curses-en.csv&quot;</span></code></pre></div>
<p>In the templates, you must prefix variables in your data file with the variable asigned to it in the config file. The content of the <code>data/pers_info-en.yaml</code> is:</p>
<div class="sourceCode"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span class="fu">family_name:</span> <span class="st">&quot;Without Name&quot;</span>
<span class="fu">name:</span> <span class="st">&quot;Name&quot;</span>
<span class="fu">fullname:</span> <span class="st">&quot;Without Name, Someone&quot;</span>
<span class="fu">address:</span> <span class="st">&quot;One Address street&quot;</span>
<span class="fu">postal_code:</span> <span class="st">&quot;00000&quot;</span>
<span class="fu">village:</span> <span class="st">&quot;The Village&quot;</span>
<span class="fu">country:</span> <span class="st">&quot;The Country&quot;</span>
<span class="fu">telephone:</span> <span class="st">&quot;+01 234 567 890&quot;</span>
<span class="fu">mobile:</span> <span class="st">&quot;+01 234 567 890&quot;</span>
<span class="fu">emails:</span>
  <span class="kw">-</span> <span class="st">&quot;someone@example.com&quot;</span>
  <span class="kw">-</span> <span class="st">&quot;name.familyname@example.com&quot;</span>

<span class="co">...</span></code></pre></div>
<p>And the use in the template file is:</p>
<pre class="django"><code>&lt;h1&gt;
{{ persinfo.fullname }}
&lt;/h1&gt;
&lt;h2&gt;
{{ persinfo.profession }}
&lt;/h2&gt;

...</code></pre>
<p>The result will be:</p>
<div class="sourceCode"><pre class="sourceCode html"><code class="sourceCode html">...
...
<span class="kw">&lt;h1&gt;</span>
Without Name, Someone
<span class="kw">&lt;/h1&gt;</span>
<span class="kw">&lt;h2&gt;</span>
Dark wizard
<span class="kw">&lt;/h2&gt;</span>

...</code></pre></div>
<h2 id="templates">Templates</h2>
<p>You can use the full power of <code>Jinja</code> in your templates. You can, for instance, check if a variable is defined, or if the variable store multiples values (arrays, lists) repeat the block of text varying the contents. From the same example, the data about emails in <code>data/pers_info-en.yaml</code>:</p>
<div class="sourceCode"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span class="co">...</span>

<span class="co">emails:</span>
<span class="co">  - &quot;someone@example.com&quot;</span>
<span class="co">  - &quot;name.familyname@example.com&quot;</span>

<span class="co">...</span></code></pre></div>
<p>The use of the data in the HTML template:</p>
<pre class='django'>
...
<code>
{% if persinfo.emails|length>0 %}
    <div class="col-sm-6">
        <strong>
        {%- if persinfo.emails|length>1 %}
            Emails
        {% else %}
            Email
        {% endif -%}
        </strong>
        <div class="email">
            <ul>
            {% for email in persinfo.emails %}<li>{{ email }}</li>{% endfor %}
            </ul>
        </div>
    </div>
{% endif %}
</code>
...
</pre>
<p>Tip: The use of a hyphen (&quot;-&quot;) at the start or end of a block permits delete white spaces or newlines between the exterior and the interior of the block.</p>
<p>The result is:</p>
<div class="sourceCode"><pre class="sourceCode html"><code class="sourceCode html"><span class="kw">&lt;div</span><span class="ot"> class=</span><span class="st">&quot;col-sm-6&quot;</span><span class="kw">&gt;</span>
    <span class="kw">&lt;strong&gt;</span>Emails<span class="kw">&lt;/strong&gt;</span>
    <span class="kw">&lt;div</span><span class="ot"> class=</span><span class="st">&quot;email&quot;</span><span class="kw">&gt;</span>
        <span class="kw">&lt;ul&gt;</span>
          <span class="kw">&lt;li&gt;</span>someone@example.com<span class="kw">&lt;/li&gt;</span>
          <span class="kw">&lt;li&gt;</span>name.familyname@example.com<span class="kw">&lt;/li&gt;</span>
        <span class="kw">&lt;/ul&gt;</span>
    <span class="kw">&lt;/div&gt;</span>
<span class="kw">&lt;/div&gt;</span></code></pre></div>
<h3 id="latex">Latex</h3>
<p>The format of <code>jinja2</code> variables and blocks in the latex templates has been changed because of the use of curly brackets in LaTeX.</p>
<p>You must change one { or } by two (( or )).</p>
<h3 id="html">HTML</h3>
<p>Note: if the final objective of the HTML file generated is to be put on a web page, then I suggest you don't put any sensitive information on the CV. For instance, do not include your address and telephone. For the email, it is better to add an obfuscating trap for bots or use a new dedicated account with a good spam filter. For good spam filter I mean that it is configurable, because in this case, it is better not to have false positives, although that implies getting more spam in the main mail folder (but you don't want to lose some contractor request in the darkness of the spam folder).</p>
<h2 id="tips">Tips</h2>
<ul>
<li><p>When modifying the template save and compile frequently to check if you do not forget to close some block. Even better if you use Git or a control version software.</p></li>
<li><p>When the value of your variable does not appear in the document generated, check if you have forgotten to put your variable inside the markers used in your template (for HTML {{ variable }} and LaTeX ((( variable ))) ).</p></li>
<li><p>If you need to write a variable inside some parenthesis, see for example <em>country</em> in europasscv and the use of &quot;-&quot;.</p>
<div class="sourceCode"><pre class="sourceCode latex"><code class="sourceCode latex">\ecvaddress{((( persinfo.address ))), ((( persinfo.postal_code ))) 
((( persinfo.village ))) ( (((- persinfo.country -))) ) }</code></pre></div></li>
<li><p>Because this workflow is in principle for your own use, you do not need to escape content of variables. If you can read about is good for you. Avoid using shell escape (\write18{}) in LaTeX and probably you are save.</p></li>
<li><p>If you need to store some of your data already formatted, then it is better if you make a subdivision of that data using the name of the format as the name of the variable. In this case, it is preferable that the variable in YAML will be stored using the | style. That permits to write in several lines using the final document syntax. As you are writing final code syntax and you control what is inside the data, you do not need to escape the variable in the template. For instance, see personal skills.</p></li>
</ul>
<p>For example, in the <code>data/pers_info-en.yaml</code> file, at the end:</p>
<div class="sourceCode"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span class="co">...</span>

<span class="co">profession: &quot;Dark wizard&quot;</span>
<span class="co">about:</span>
<span class="co">  html: |</span>
<span class="co">    I am, of course, the &lt;strong&gt;best in the world&lt;/strong&gt; in the things I do. </span>
<span class="co">    I was born sometime ago in a place where &quot;the rule is not born by your own </span>
<span class="co">    means&quot;, your mother was there with you. My mother told me, this should be </span>
<span class="co">    the last time that you born all by yourself (homage to </span>
<span class="co">    &lt;a href=&quot;https://en.wikipedia.org/wiki/Miguel_Gila&quot;&gt;Miguel Gila&lt;/a&gt;). </span>

<span class="co">    When I was a little kid, I also started to walk alone. When I was a teenager, </span>
<span class="co">    you know... After that, I never started a startup, I was never the best in </span>
<span class="co">    anything, so, if you want to hire me, you must know who I am. </span>
<span class="co">  latex: |</span>
<span class="co">    I am, of course, the \textbf{best in the world} in the things I do. </span>
<span class="co">    I was born sometime ago in a place where &quot;the rule is not born by your own </span>
<span class="co">    means&quot;, your mother was there with you. My mother told me, this should be </span>
<span class="co">    the last time that you born all by yourself (homage to </span>
<span class="co">    \href{https://en.wikipedia.org/wiki/Miguel_Gila}{Miguel Gila}). </span>

<span class="co">    When I was a little kid, I also started to walk alone. When I was a teenager, </span>
<span class="co">    you know... After that, I never started a startup, I was never the best in </span>
<span class="co">    anything, so, if you want to hire me, you must know who I am.</span>

<span class="co">...</span></code></pre></div>
<p>You write markup directly for both HTML and LaTeX in two different variables behind the same parent variable <code>about</code>. You then use it in the template as:</p>
<pre class="django"><code>{% if persinfo.about.html is defined %}
  &lt;section id=&quot;about&quot; class=&quot;row&quot;&gt;
    &lt;aside class=&quot;col-sm-3&quot;&gt;
    &lt;h3&gt;About&lt;/h3&gt;
    &lt;/aside&gt;
    &lt;div class=&quot;col-sm-9&quot;&gt;
    &lt;p&gt;{{ persinfo.about.html }}&lt;/p&gt;
    &lt;/div&gt;
  &lt;/section&gt;
{% endif %}</code></pre>
<ul>
<li>For use <code>csv</code> tabular data, see the example file <code>acad_info_curses-en.csv</code>:</li>
</ul>
<pre class="csv"><code>name,year
How to make cakes, 2000
How to not eat the cakes you cooked, 2001</code></pre>
<pre><code>It is declared in the data section of the config file as `curses`, and it is used in the html template example:</code></pre>
<pre class="django"><code>{% if curses is defined %}

&lt;section id=&quot;curses&quot; class=&quot;row&quot;&gt;
&lt;aside class=&quot;col-sm-3&quot;&gt;
  &lt;h3&gt;Curses&lt;/h3&gt;
&lt;/aside&gt;
{% for curse in curses %}
  &lt;h4 class=&quot;strike-through&quot;&gt;
  &lt;span&gt;{{ curse.name }}&lt;/span&gt;
  &lt;span class=&quot;date&quot;&gt;
  {{ curse.year }}
  &lt;/span&gt;
  &lt;/h4&gt;
{% endfor %}
&lt;/section&gt;
{% endif %}</code></pre>
<pre><code>And the result:</code></pre>
<div class="sourceCode"><pre class="sourceCode html"><code class="sourceCode html"><span class="kw">&lt;section</span><span class="ot"> id=</span><span class="st">&quot;curses&quot;</span><span class="ot"> class=</span><span class="st">&quot;row&quot;</span><span class="kw">&gt;</span>
  <span class="kw">&lt;aside</span><span class="ot"> class=</span><span class="st">&quot;col-sm-3&quot;</span><span class="kw">&gt;</span>
    <span class="kw">&lt;h3&gt;</span>Curses<span class="kw">&lt;/h3&gt;</span>
  <span class="kw">&lt;/aside&gt;</span>
  <span class="kw">&lt;h4</span><span class="ot"> class=</span><span class="st">&quot;strike-through&quot;</span><span class="kw">&gt;</span>
  <span class="kw">&lt;span&gt;</span>How to make cakes<span class="kw">&lt;/span&gt;</span>
  <span class="kw">&lt;span</span><span class="ot"> class=</span><span class="st">&quot;date&quot;</span><span class="kw">&gt;</span>
    2000
  <span class="kw">&lt;/span&gt;</span>
  <span class="kw">&lt;/h4&gt;</span>
  <span class="kw">&lt;h4</span><span class="ot"> class=</span><span class="st">&quot;strike-through&quot;</span><span class="kw">&gt;</span>
  <span class="kw">&lt;span&gt;</span>How to not eat the cakes you cooked<span class="kw">&lt;/span&gt;</span>
  <span class="kw">&lt;span</span><span class="ot"> class=</span><span class="st">&quot;date&quot;</span><span class="kw">&gt;</span>
    2001
  <span class="kw">&lt;/span&gt;</span>
  <span class="kw">&lt;/h4&gt;</span></code></pre></div>
