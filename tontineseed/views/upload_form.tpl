% rebase('base.tpl', title='HOME PAGE')

          <div class="inner cover">
            <p> Upload torrent here. Max size is 20 MB.</p>
            <form action="/upload" method="post" enctype="multipart/form-data">
                <input type="file" name="data" />
                <input type="submit" value="Submit">
            </form>
          
          </div>
