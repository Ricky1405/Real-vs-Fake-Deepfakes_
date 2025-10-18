def commit_callback(commit):
    if commit.author_email == b"divyamaakarsh22@gmail.com":
        commit.author_name = b"Ricky1405"
        commit.author_email = b"vikramummiti@gmail.com"
    if commit.committer_email == b"divyamaakarsh22@gmail.com":
        commit.committer_name = b"Ricky1405"
        commit.committer_email = b"vikramummiti@gmail.com"
