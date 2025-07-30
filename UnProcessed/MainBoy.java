import java.util.Arrays;




public class MainBoy {


    public static int gcd(int a,int b){
        if (a%b == 0){
            return b;
        }
        else{
            return gcd(b, a%b);
        }

    }

    


    public static int[] merging(int[] arr1, int[] arr2){
        int pointer1 = 0;
        int pointer2 = 0;
        int temparrpointer = 0;
        int[] temparr = new int[arr1.length+arr2.length];

        while (pointer1 < arr1.length && pointer2 < arr2.length){
            
            if (arr1[pointer1]<arr2[pointer2]){
                temparr[temparrpointer] = arr1[pointer1];
                pointer1++;
                temparrpointer++;
            }
            else{
                temparr[temparrpointer] = arr2[pointer2];
                pointer2++;
                temparrpointer++;
            }
        }
        
        
        while (pointer1 < arr1.length){
            temparr[temparrpointer] = arr1[pointer1];
            pointer1++;
            temparrpointer++;

        }

        while (pointer2 < arr2.length){
            temparr[temparrpointer] = arr2[pointer2];
            pointer2++;
            temparrpointer++;
            
        }
        
        System.out.println(Arrays.toString(temparr));
        
        return temparr;
    }




    public static int[] mergesort(int[] sortyarr){
        if (sortyarr.length == 1){
            return sortyarr;
        }
        
        int bisect = sortyarr.length/2;
        int[] arr1 = new int[bisect];
        int[] arr2 = new int[sortyarr.length-bisect];

        for(int o = 0; o < bisect; o++){
            arr1[o] = sortyarr[o];
        }

        for(int z = 0; z < sortyarr.length-bisect; z++){
            arr2[z] = sortyarr[bisect+z];
        }

        return merging(mergesort(arr1),mergesort(arr2));
    }

    public static void dfs(int index, int[] visitarr, int[][] adjarr){
        visitarr[index]=1;
        for (int jum : adjarr[index]){
            if (visitarr[jum]<1){
                dfs(jum,visitarr,adjarr);
            }
        }
        System.out.println(Arrays.toString(visitarr));
        ;
    }
    public static void main(String[] args) {

        int size = 5;
        int[] visits =  new int[size];
        int[][] adj = {{1,4},{0,2,3},{1},{1,4},{0,3}};

        for(int j = 0; j<size; j++){
            if (visits[j]==0){
                System.out.println(j);
                dfs(j,visits,adj);
            }
        }

        // FloydWarshall Test

        int numnodes = 5;
        int[][] hx = {{2,3,7},{3,4,2},{0,4,1},{0,3,9},{0,1,5},{1,2,2}};


        int[][] adjacencymatrix = new int[numnodes][numnodes];

        for(int x = 0; x<numnodes; x++){
            for(int y = 0; y < numnodes; y++){
                if (x==y){
                    adjacencymatrix[x][y]=0;
                }
                else{
                    adjacencymatrix[x][y] = 1000000;
                }
            }
        }

        for(int[] pair : hx){
            adjacencymatrix[pair[0]][pair[1]] = pair[2];
            adjacencymatrix[pair[1]][pair[0]] = pair[2];
        }

        for (int i = 0; i<numnodes;i++){
            for (int j = 0; j<numnodes;j++){
                for (int maximizer = 0; maximizer<numnodes;maximizer++){

                    adjacencymatrix[i][j] = Math.min(adjacencymatrix[i][maximizer]+adjacencymatrix[j][maximizer],adjacencymatrix[i][j]);
                    adjacencymatrix[j][i] = Math.min(adjacencymatrix[i][maximizer]+adjacencymatrix[j][maximizer],adjacencymatrix[j][i]);
                }
            }
        }

        for (int i = 0; i<numnodes;i++){
            for (int j = 0; j<numnodes;j++){
                System.out.print(adjacencymatrix[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println(gcd(21,14));


        int[] arrby = {1,6,7,0,9,2};

        System.out.println(Arrays.toString(mergesort(arrby)));


        try {
            int bruh = 10/1;
            System.out.println("sus");

        }
        catch(Exception e){
            System.out.println("bruh");
        }
        finally{
            System.out.println("DUM");
        }
        
    }
}










// Double.POSITIVE_INFINITY