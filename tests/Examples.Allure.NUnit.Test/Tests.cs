using NUnit.Allure.Core;
using NUnit.Framework;
using Allure.NUnit.Attributes;

[TestFixture]
[AllureNUnit]
public class Tests
{
    [Test]
    [Ignore("Причина игнорирования теста")]
    public void IgnoredTest()
    {
        Assert.Pass();
    }
    
    [Test2]
    public void WorkingTest()
    {
        Assert.Pass();
    }
}
