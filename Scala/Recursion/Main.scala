package recfun

object Main {
  def main(args: Array[String]) {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }
  }


  /**
   * Exercise 1
   */
    def pascal(c: Int, r: Int): Int = {
      if ( c < 0 || r < 0 ) 0
      else if ( c > r ) 0
      else if ( c == 0 || r == 0 ) 1
      else if ( c == r ) 1
      else pascal( c - 1, r - 1) + pascal( c, r - 1 )
    }
  
  /**
   * Exercise 2
   */
    def balance(chars: List[Char]): Boolean = {
      def balanceIter(chars: List[Char], count: Int): Boolean = {
        if (chars.isEmpty &&  count == 0) true
        else if (count < 0) false
        else if (chars.head == '(') balanceIter(chars.tail, count+1)
        else if (chars.head == ')') balanceIter(chars.tail, count-1)
        else balanceIter(chars.tail, count)
      }
      if (chars.isEmpty) true
      else balanceIter(chars,0)
    }
  
  /**
   * Exercise 3
   */
    def countChange(money: Int, coins: List[Int]): Int = {
      if (money < 0 || coins.isEmpty) 0
      else if (coins.length == 1 && coins.head == 0) 0
      else if (money == 0) 1
      else if(money > 0 && !coins.isEmpty) countChange(money - coins.head, coins.distinct) + countChange(money, coins.distinct.tail)
      else 0
    }
  }
