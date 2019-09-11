class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = []

        for part in path.split("/"):
            if part == "" or part == ".":
                # barras repetidas o carpeta actual: no cambian nada
                continue
            if part == "..":
                if folders:
                    folders.pop()
            else:
                folders.append(part)

        return "/" + "/".join(folders)


if __name__ == "__main__":
    s = Solution()

    assert s.simplifyPath("/home/") == "/home"
    assert s.simplifyPath("/home//foo/") == "/home/foo"
    assert s.simplifyPath("/home/user/Documents/../Pictures") == "/home/user/Pictures"
    assert s.simplifyPath("/../") == "/"
    assert s.simplifyPath("/.../a/../b/c/../d/./") == "/.../b/d"

    assert s.simplifyPath("/") == "/"
    assert s.simplifyPath("/a/./b/../../c/") == "/c"
    assert s.simplifyPath("/home/../../..") == "/"
    assert s.simplifyPath("/a//b////c/d//././/..") == "/a/b/c"
    assert s.simplifyPath("/..hidden/.../_x") == "/..hidden/.../_x"

    print("ok")
