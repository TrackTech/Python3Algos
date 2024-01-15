import typing
def count_valid_emails(pattern:str)->int:

    max_count = 0

    def dfs(index,path,state,has_at):
        if index>=len(pattern):
            curr=1
            for s in state:
                curr*=s
            max_count=max(max_count,curr)
            return
        
        for i in range(index,len(pattern)):
            if pattern[i]!='?':
                state.append(1)
                path.append(pattern[i])
            else:
                if has_at:
                    

        



    return 0